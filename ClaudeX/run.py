"""
claudeaffinity.py
=================
NPB (CG / MG) の 1 実験エントリーポイント。
下の「実験設定」セクションの変数を変更して実行する。

  python3 claudeaffinity.py
"""

import os
import subprocess
from datetime import datetime

from utility.cpu_affinity  import get_cpu_map, STRATEGY_DESC, patch_cpu_map, recompile_workload, NPB_BIN_DIR
from utility.stats_reader  import parse_node_stats, print_summary
from utility.grapher       import generate_numa_graph
from utility.config_writer import save_affinity_config

# ============================================================
# 実験設定（ここを編集して実験を変更する）
# ============================================================
WORKLOAD    = "CG"        # CG / MG
STRATEGY    = "Scatter"   # Packed / Scatter / HPO / MPO / SPO
BENCH_CLASS = "S"         # S / W / A / B / C / D
NUM_THREADS = 2

# カスタム cpu_map を使う場合は 16 個の CPU ID を列挙する（None でストラテジーを使用）
CUSTOM_MAP  = None
# ============================================================

GEM5        = "/home/hiragahama/gem5/build/X86/gem5.opt"
MYEXP       = "/home/hiragahama/gem5/ClaudeX/gem5_sim.py"
CLAUDEX_DIR = "/home/hiragahama/gem5/ClaudeX"
OUTPUT_BASE = "/home/hiragahama/gem5/ClaudeX/Outputs"

NUM_NODES = 2
BIG_CPN   = 4
SML_CPN   = 4


def run_gem5(binary: str, strategy: str, num_threads: int) -> str:
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = os.path.join(
        OUTPUT_BASE, f"{WORKLOAD}_{BENCH_CLASS}_{strategy}_{num_threads}TH_{now}"
    )
    os.makedirs(output_dir, exist_ok=True)

    cmd = [
        GEM5, "-d", output_dir,
        MYEXP,
        f"--strategy={strategy}",
        f"--num-threads={num_threads}",
        f"--binary={binary}",
        "--num-nodes=2",
    ]
    print(f"[gem5] 実行開始 → {output_dir}")
    subprocess.run(cmd, cwd=CLAUDEX_DIR, check=True)
    print("[gem5] 完了")
    return output_dir


def main():
    cpu_map       = CUSTOM_MAP if CUSTOM_MAP else get_cpu_map(STRATEGY, WORKLOAD)
    strategy_name = "custom" if CUSTOM_MAP else STRATEGY
    wl            = WORKLOAD.lower()
    binary        = os.path.join(NPB_BIN_DIR, f"{wl}.{BENCH_CLASS}.x")

    print(f"\n[設定]")
    print(f"  ワークロード : {WORKLOAD}")
    print(f"  ストラテジー : {strategy_name}  ({STRATEGY_DESC.get(strategy_name, '')})")
    print(f"  スレッド数   : {NUM_THREADS}")
    print(f"  クラス       : {BENCH_CLASS}")
    print(f"  cpu_map      : {cpu_map}")

    patch_cpu_map(cpu_map, WORKLOAD)
    recompile_workload(WORKLOAD, BENCH_CLASS)

    output_dir = run_gem5(binary, strategy_name, NUM_THREADS)

    save_affinity_config(output_dir, strategy_name, WORKLOAD, BENCH_CLASS,
                         cpu_map, NUM_THREADS, NUM_NODES, BIG_CPN, SML_CPN)

    node_stats = parse_node_stats(output_dir, NUM_NODES)
    generate_numa_graph(output_dir, node_stats, strategy_name,
                        cpu_map, NUM_THREADS, WORKLOAD, BENCH_CLASS)
    print_summary(node_stats, cpu_map, NUM_THREADS)

    print(f"\n[完了] {output_dir}")


if __name__ == "__main__":
    main()
