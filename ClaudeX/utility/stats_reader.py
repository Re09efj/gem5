"""
stats_reader.py
gem5 stats.txt から NUMA ノード別メモリアクセス数を読み取る。
"""

import os
import re


def parse_node_stats(output_dir: str, num_nodes: int = 2) -> dict:
    """stats.txt を読んで {node_id: {"reads": int, "writes": int}} を返す。"""
    stats_file = os.path.join(output_dir, "stats.txt")
    if not os.path.exists(stats_file):
        print(f"[WARN] stats.txt が見つかりません: {stats_file}")
        return {}

    with open(stats_file) as f:
        content = f.read()

    result = {}
    for i in range(num_nodes):
        r = re.search(rf"system\.mem_ctrl{i}\.readReqs\s+(\d+)", content)
        w = re.search(rf"system\.mem_ctrl{i}\.writeReqs\s+(\d+)", content)
        result[i] = {
            "reads":  int(r.group(1)) if r else 0,
            "writes": int(w.group(1)) if w else 0,
        }
    return result


def print_summary(node_stats: dict, cpu_map: list, num_threads: int) -> None:
    """NUMA アクセス集計をターミナルに表示する。"""
    if not node_stats:
        return

    total_r = sum(v["reads"]  for v in node_stats.values())
    total_w = sum(v["writes"] for v in node_stats.values())
    grand   = total_r + total_w

    cpu_ranges = {0: "CPU  0- 7", 1: "CPU  8-15"}

    print("\n" + "=" * 62)
    print("  NUMA メモリアクセス集計")
    print("=" * 62)
    for n, stats in node_stats.items():
        total = stats["reads"] + stats["writes"]
        ratio = total / grand * 100 if grand > 0 else 0
        print(f"  Node {n} ({cpu_ranges.get(n, f'Node{n}')}):")
        print(f"    reads  = {stats['reads']:>14,}")
        print(f"    writes = {stats['writes']:>14,}")
        print(f"    合計   = {total:>14,}  ({ratio:.1f}%)")
    print("-" * 62)
    print(f"  全体合計: reads={total_r:,}  writes={total_w:,}")
    print("\n  スレッド → CPU → ノード マッピング:")
    for t in range(min(num_threads, 16)):
        cpu   = cpu_map[t]
        node  = 0 if cpu < 8 else 1
        ctype = "P" if (cpu % 8) < 4 else "E"
        print(f"    thread {t:2d} → CPU {cpu:2d}  (Node {node}, {ctype}-core)")
    print("=" * 62)
