"""
orchestrator.py
===============
複数のワークロード x アフィニティ戦略を統括して実行する。
下の「実験設定」セクションの変数を変更して実行する。

  python3 orchestrator.py
"""

import os
import subprocess
from concurrent.futures import (
    ThreadPoolExecutor,
    as_completed,
)
from datetime import datetime

from utility.config_writer import save_affinity_config
from utility.cpu_affinity import (
    compile_strategy,
    get_cpu_map,
)
from utility.grapher import generate_numa_graph
from utility.stats_reader import parse_node_stats

# ============================================================
# 実験設定（ここを編集して実験を変更する）
# ============================================================
WORKLOADS = ["CG", "MG"]  # 実行するワークロード
BENCH_CLASS = "S"  # S / W / A / B / C / D
NUM_THREADS = 2  # OMP_NUM_THREADS
STRATEGIES_TO_RUN = ["Packed", "Scatter", "HPO", "MPO"]  # 実行するストラテジー
WORKERS = 8  # gem5 最大並列実行数
# ============================================================

GEM5 = "/home/hiragahama/gem5/build/X86/gem5.opt"
MYEXP = "/home/hiragahama/gem5/ClaudeX/gem5_sim.py"
CLAUDEX_DIR = "/home/hiragahama/gem5/ClaudeX"
OUTPUT_BASE = "/home/hiragahama/gem5/ClaudeX/Outputs"

NUM_NODES = 2
BIG_CPN = 4
SML_CPN = 4


# ── ヘルパー ─────────────────────────────────────────────────


def _core_label(cpu: int) -> str:
    node = 0 if cpu < 8 else 1
    ctype = "P" if (cpu % 8) < 4 else "E"
    return f"C{cpu}(N{node}{ctype})"


# ── STEP 1: コンパイル ────────────────────────────────────────


def _compile_workload(workload: str) -> dict[str, str]:
    """1ワークロード分の全ストラテジーを逐次コンパイルして {strategy: binary_path} を返す。
    ワークロード間は独立した numa_affinity.c を持つため並列呼び出し可能。"""
    binaries = {}
    for strategy in STRATEGIES_TO_RUN:
        cpu_map = get_cpu_map(strategy, workload)
        binaries[strategy] = compile_strategy(
            strategy, cpu_map, workload, BENCH_CLASS
        )
    return binaries


def _compile_all() -> dict[str, dict[str, str]]:
    """全ワークロードをワークロード間並列でコンパイルする。"""
    print(
        f"\n[STEP 1] コンパイル ({len(WORKLOADS)} ワークロード, ワークロード間並列)"
    )
    all_binaries: dict[str, dict[str, str]] = {}
    with ThreadPoolExecutor(max_workers=len(WORKLOADS)) as ex:
        futures = {ex.submit(_compile_workload, wl): wl for wl in WORKLOADS}
        for future in as_completed(futures):
            wl = futures[future]
            try:
                all_binaries[wl] = future.result()
            except Exception as e:
                print(f"[ERROR:compile:{wl}] {e}")
                all_binaries[wl] = {}
    return all_binaries


# ── STEP 2: gem5 実行 ────────────────────────────────────────


def _run_gem5(binary: str, workload: str, strategy: str, run_id: str) -> str:
    output_dir = os.path.join(
        OUTPUT_BASE,
        f"{workload}_{BENCH_CLASS}_{strategy}_{NUM_THREADS}TH_{run_id}",
    )
    os.makedirs(output_dir, exist_ok=True)
    cmd = [
        GEM5,
        "-d",
        output_dir,
        MYEXP,
        f"--strategy={strategy}",
        f"--num-threads={NUM_THREADS}",
        f"--binary={binary}",
        "--num-nodes=2",
    ]
    print(f"[gem5:{workload}/{strategy}] 開始")
    subprocess.run(
        cmd,
        cwd=CLAUDEX_DIR,
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    print(f"[gem5:{workload}/{strategy}] 完了")
    return output_dir


def _run_all_gem5(
    all_binaries: dict, run_id: str
) -> dict[tuple[str, str], str]:
    """全 (workload, strategy) 組み合わせを WORKERS 上限で並列実行する。"""
    total = sum(len(b) for b in all_binaries.values())
    print(f"\n[STEP 2] gem5 並列実行 ({total} 実験, workers={WORKERS})")
    output_dirs: dict[tuple[str, str], str] = {}
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futures = {
            ex.submit(_run_gem5, binary, wl, strategy, run_id): (wl, strategy)
            for wl, strategies in all_binaries.items()
            for strategy, binary in strategies.items()
        }
        for future in as_completed(futures):
            key = futures[future]
            try:
                output_dirs[key] = future.result()
            except Exception as e:
                print(f"[ERROR:{key[0]}/{key[1]}] gem5 失敗: {e}")
    return output_dirs


# ── STEP 3: 結果収集 ─────────────────────────────────────────


def _collect_results(output_dirs: dict) -> dict[str, list]:
    """stats 解析・グラフ生成・config 保存を行い、ワークロード別の結果リストを返す。"""
    print(f"\n[STEP 3] 結果収集")
    results: dict[str, list] = {wl: [] for wl in WORKLOADS}
    for wl in WORKLOADS:
        for strategy in STRATEGIES_TO_RUN:
            output_dir = output_dirs.get((wl, strategy))
            if not output_dir:
                continue
            cpu_map = get_cpu_map(strategy, wl)
            node_stats = parse_node_stats(output_dir, NUM_NODES)
            save_affinity_config(
                output_dir,
                strategy,
                wl,
                BENCH_CLASS,
                cpu_map,
                NUM_THREADS,
                NUM_NODES,
                BIG_CPN,
                SML_CPN,
            )
            generate_numa_graph(
                output_dir,
                node_stats,
                strategy,
                cpu_map,
                NUM_THREADS,
                wl,
                BENCH_CLASS,
            )
            results[wl].append(
                {
                    "strategy": strategy,
                    "node_stats": node_stats,
                    "cpu_map": cpu_map,
                }
            )
    return results


# ── サマリー表示 ─────────────────────────────────────────────


def _print_summary(results: dict, run_id: str) -> None:
    print(f"\n{'='*76}")
    print(
        f"  全実験結果サマリー  (Class {BENCH_CLASS}, {NUM_THREADS} threads)"
    )
    print(f"{'='*76}")
    print(
        f"  {'WL':<4} {'Strategy':<10}  {'Node0':>10}  {'Node1':>10}  {'Node0%':>7}  使用コア"
    )
    print(f"  {'-'*72}")
    for wl in WORKLOADS:
        for r in results[wl]:
            ns = r["node_stats"]
            t0 = ns.get(0, {}).get("reads", 0) + ns.get(0, {}).get("writes", 0)
            t1 = ns.get(1, {}).get("reads", 0) + ns.get(1, {}).get("writes", 0)
            grand = t0 + t1
            ratio = t0 / grand * 100 if grand > 0 else 0
            cmap = r["cpu_map"]
            cores = " ".join(
                f"T{t}→{_core_label(cmap[t])}"
                for t in range(min(NUM_THREADS, 4))
            )
            if NUM_THREADS > 4:
                cores += " ..."
            print(
                f"  {wl:<4} {r['strategy']:<10}  {t0:>10,}  {t1:>10,}  {ratio:>6.1f}%  {cores}"
            )
        if wl != WORKLOADS[-1]:
            print(f"  {'-'*72}")
    print(f"{'='*76}")
    print(
        f"\n  各実験出力: {OUTPUT_BASE}/{{WL}}_{BENCH_CLASS}_*_{NUM_THREADS}TH_{run_id}/"
    )


# ── エントリーポイント ────────────────────────────────────────


def main():
    run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    total = len(WORKLOADS) * len(STRATEGIES_TO_RUN)
    print(f"\n{'='*60}")
    print(f"  NUMA アフィニティ実験 オーケストレーター")
    print(
        f"  ワークロード: {WORKLOADS}  クラス={BENCH_CLASS}  スレッド数={NUM_THREADS}"
    )
    print(f"  ストラテジー: {STRATEGIES_TO_RUN}  実験数: {total}")
    print(f"{'='*60}")

    all_binaries = _compile_all()
    output_dirs = _run_all_gem5(all_binaries, run_id)
    results = _collect_results(output_dirs)
    _print_summary(results, run_id)


if __name__ == "__main__":
    main()
