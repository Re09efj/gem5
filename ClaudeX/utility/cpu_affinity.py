"""
cpu_affinity.py
numa_affinity.c の cpu_map 書き換えと NPB ワークロードのコンパイルを担当する。

対応ワークロード: CG, MG

ストラテジー定義:
  Packed  : ローカル側（Node0）P-core に集中配置
  Scatter : 複数 NUMA ノードへ分散配置（インターリーブ）
  HPO     : 性能コア（P-core）優先割り当て
             4スレッドまで全て Node0 P-core、5〜8 で Node1 P-core、以降 E-core
  MPO     : メモリ親和性優先（ワークロード依存）
             CG: first-touch で z/p が Node0 に確保 → Node0 先詰め
             MG: 3D格子の隣接スラブ担当スレッドを同ノードに → ペア配置
  SPO     : スケジューリング優先度協調制御（暫定: Scatter 配置）
"""

import os
import re
import shutil
import subprocess
import sys

NPB_OMP_DIR = "/home/hiragahama/gem5/ClaudeX/binary/NPB3.4.4/NPB3.4-OMP"
NPB_BIN_DIR = os.path.join(NPB_OMP_DIR, "bin")

# NUMA レイアウト
# Node 0: CPU  0- 3 (P-core), CPU  4- 7 (E-core)
# Node 1: CPU  8-11 (P-core), CPU 12-15 (E-core)

STRATEGIES = {
    # ─── Packed ────────────────────────────────────────────────
    # Node0 P-core → Node0 E-core の順に詰める（Node0 内で完結）
    "Packed": [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,  # threads  0- 7: Node0 (P→E)
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,  # threads  8-15: 折り返し（通常未使用）
    ],
    # ─── Scatter ───────────────────────────────────────────────
    # Node0/Node1 を交互に割り当て、メモリ帯域を両ノードに分散
    "Scatter": [
        0,
        8,
        1,
        9,
        2,
        10,
        3,
        11,  # threads  0- 7: P-core インターリーブ
        4,
        12,
        5,
        13,
        6,
        14,
        7,
        15,  # threads  8-15: E-core インターリーブ
    ],
    # ─── HPO（Heuristic Priority Ordering）────────────────────
    # P-core を全優先。Node0 P → Node1 P → Node0 E → Node1 E の順
    # スレッド数が 4 以下なら全て Node0 P-core に収まる
    "HPO": [
        0,
        1,
        2,
        3,  # threads 0-3: Node0 P-core（4スレッドまでここで完結）
        8,
        9,
        10,
        11,  # threads 4-7: Node1 P-core（5スレッド目からこちら）
        4,
        5,
        6,
        7,  # threads 8-11: Node0 E-core
        12,
        13,
        14,
        15,  # threads12-15: Node1 E-core
    ],
    # ─── SPO（Scheduling Priority Ordering）暫定 ──────────────
    # スケジューリング優先度の協調制御。cpu_map は後で設計予定。
    # 暫定として Scatter と同じ配置を使用する。
    "SPO": [
        0,
        8,
        1,
        9,
        2,
        10,
        3,
        11,  # threads  0- 7: Scatter と同じ（暫定）
        4,
        12,
        5,
        13,
        6,
        14,
        7,
        15,  # threads  8-15: 同上
    ],
}

# MPO はワークロード依存のため別定義
MPO_MAPS = {
    # CG: SpMV で全スレッドが共有密ベクトル z/p を読む。
    # first-touch によりこれらは Node0 に確保されるため Node0 先詰め。
    "CG": [
        0,
        1,
        2,
        3,  # threads 0-3: Node0 P-core（z/p がここにある）
        8,
        9,
        10,
        11,  # threads 4-7: Node1 P-core（帯域補強）
        4,
        5,
        6,
        7,  # threads 8-11: Node0 E-core
        12,
        13,
        14,
        15,  # threads12-15: Node1 E-core
    ],
    # MG: 3D格子をスラブ分割。隣接スラブを持つスレッドが境界で通信するため
    # 隣接スレッドペアを同一ノードに配置してノード内通信を最大化する。
    # (T0,T1)→Node0, (T2,T3)→Node1, (T4,T5)→Node0, ...
    "MG": [
        0,
        1,
        8,
        9,  # threads 0-3: T0,T1=Node0P / T2,T3=Node1P
        2,
        3,
        10,
        11,  # threads 4-7: T4,T5=Node0P / T6,T7=Node1P
        4,
        5,
        12,
        13,  # threads 8-11: E-core ペア
        6,
        7,
        14,
        15,  # threads12-15: E-core ペア
    ],
}

STRATEGY_DESC = {
    "Packed": "全スレッド → Node0 集中 (P→E順)",
    "Scatter": "ノード間インターリーブ (帯域分散)",
    "HPO": "P-core 優先: Node0 P → Node1 P → E-core",
    "MPO": "メモリ親和性優先 (ワークロード依存: CG=Node0先詰め / MG=隣接ペア同ノード)",
    "SPO": "スケジューリング優先度協調制御 (暫定: Scatter 配置)",
}


def get_cpu_map(strategy: str, workload: str) -> list:
    """ストラテジーとワークロードから cpu_map を返す。MPO のみワークロード依存。"""
    if strategy == "MPO":
        key = workload.upper()
        if key not in MPO_MAPS:
            print(
                f"[WARNING] MPO map for '{workload}' 未定義。CG 配置を使用します。"
            )
            key = "CG"
        return MPO_MAPS[key]
    if strategy not in STRATEGIES:
        print(f"[ERROR] 不明なストラテジー: {strategy}")
        sys.exit(1)
    return STRATEGIES[strategy]


def _affinity_c_path(workload: str) -> str:
    return os.path.join(NPB_OMP_DIR, workload.upper(), "numa_affinity.c")


def patch_cpu_map(cpu_map: list, workload: str) -> None:
    path = _affinity_c_path(workload)
    with open(path) as f:
        src = f.read()

    pattern = r"static int cpu_map\[16\]\s*=\s*\{[^}]+\};"
    if not re.search(pattern, src, flags=re.DOTALL):
        print(f"[ERROR] cpu_map パターンが見つかりません: {path}")
        sys.exit(1)

    line0 = ", ".join(str(x) for x in cpu_map[:8])
    line1 = ", ".join(str(x) for x in cpu_map[8:])
    new_block = (
        f"static int cpu_map[16] = {{\n"
        f"    {line0},\n"
        f"    {line1}\n"
        f"}};"
    )
    patched = re.sub(pattern, new_block, src, flags=re.DOTALL)
    with open(path, "w") as f:
        f.write(patched)
    print(f"[patch] {workload}/numa_affinity.c 更新: {cpu_map}")


def recompile_workload(workload: str, bench_class: str = "S") -> None:
    """ワークロード（CG / MG など）のバイナリを再コンパイルする。gem5 本体は触らない。"""
    target = workload.lower()
    print(f"[compile] make {target} CLASS={bench_class} ...")
    result = subprocess.run(
        ["make", target, f"CLASS={bench_class}"],
        cwd=NPB_OMP_DIR,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"[ERROR] コンパイル失敗 ({workload})")
        print(result.stderr[-2000:])
        sys.exit(1)
    print(f"[compile] {workload} Class {bench_class} 完了")


def compile_strategy(
    strategy_name: str, cpu_map: list, workload: str, bench_class: str = "S"
) -> str:
    """patch → compile → バイナリをストラテジー名付きでコピーして返す。
    orchestrator が並列 gem5 実行のために各ストラテジーごとに独立バイナリを作る。"""
    patch_cpu_map(cpu_map, workload)
    recompile_workload(workload, bench_class)
    wl = workload.lower()
    src = os.path.join(NPB_BIN_DIR, f"{wl}.{bench_class}.x")
    dst = os.path.join(NPB_BIN_DIR, f"{wl}.{bench_class}.{strategy_name}.x")
    shutil.copy2(src, dst)
    print(f"[binary] {dst}")
    return dst
