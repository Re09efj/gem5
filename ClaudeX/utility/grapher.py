"""
grapher.py
3 種類のグラフを生成する。
  1. generate_core_stats_graph  - CPI / Cycles per core
  2. generate_numa_graph        - 単一実験の Node0/Node1 アクセス比較
  3. generate_comparison_graph  - 複数プリセット横断比較（orchestrator 用）
"""

import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# ─────────────────────────────────────────────
# 1. CPI / Cycles per core
# ─────────────────────────────────────────────
def generate_core_stats_graph(
    csv_path: str, num_nodes: int, big_cpn: int, sml_cpn: int
) -> None:
    if not os.path.exists(csv_path):
        print(f"[grapher] CSV が見つかりません: {csv_path}")
        return

    df = pd.read_csv(csv_path)
    cores_per_node = big_cpn + sml_cpn
    cpi_data, cycles_data = [], []

    for node_id in range(num_nodes):
        for cpu_id in range(cores_per_node):
            label = (
                f"N{node_id}-{'Big' if cpu_id < big_cpn else 'Small'}{cpu_id}"
            )
            stat_base = f"system.cpus{cpu_id}"

            cpi_row = df[df["stat_name"] == f"{stat_base}.cpi"]
            if not cpi_row.empty:
                cpi_data.append(
                    {
                        "Core": label,
                        "CPI": float(cpi_row.iloc[0]["value"]),
                        "NodeID": node_id,
                        "CoreType": "Big" if cpu_id < big_cpn else "Small",
                    }
                )

            cyc_row = df[df["stat_name"] == f"{stat_base}.numCycles"]
            if not cyc_row.empty:
                cycles_data.append(
                    {
                        "Core": label,
                        "NumCycles": int(cyc_row.iloc[0]["value"]),
                        "NodeID": node_id,
                        "CoreType": "Big" if cpu_id < big_cpn else "Small",
                    }
                )

    df_cpi = pd.DataFrame(cpi_data)
    df_cycles = pd.DataFrame(cycles_data)
    if df_cpi.empty or df_cycles.empty:
        print("[grapher] 警告: CPI/Cycles データが見つかりませんでした。")
        return

    type_palette = {"Big": "steelblue", "Small": "tomato"}
    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(1, 2, figsize=(18, 6))

    sns.barplot(
        x="Core",
        y="CPI",
        data=df_cpi,
        hue="CoreType",
        palette=type_palette,
        ax=axes[0],
        legend=True,
        dodge=False,
    )
    axes[0].set_title(
        "CPI per Core (Lower is Better)", fontsize=14, fontweight="bold"
    )
    axes[0].set_xlabel("CPU Cores", fontsize=12)
    axes[0].set_ylabel("CPI (Cycles Per Instruction)", fontsize=12)
    axes[0].tick_params(axis="x", rotation=45)
    for p in axes[0].patches:
        if p.get_height() > 0:
            axes[0].annotate(
                f"{p.get_height():.2f}",
                (p.get_x() + p.get_width() / 2.0, p.get_height()),
                ha="center",
                va="bottom",
                xytext=(0, 4),
                textcoords="offset points",
                fontsize=8,
            )

    sns.barplot(
        x="Core",
        y="NumCycles",
        data=df_cycles,
        hue="CoreType",
        palette=type_palette,
        ax=axes[1],
        legend=True,
        dodge=False,
    )
    axes[1].set_title("Total Cycles per Core", fontsize=14, fontweight="bold")
    axes[1].set_xlabel("CPU Cores", fontsize=12)
    axes[1].set_ylabel("Number of Cycles", fontsize=12)
    axes[1].tick_params(axis="x", rotation=45)

    plt.tight_layout()
    out = os.path.join(os.path.dirname(csv_path), "core_stats_summary.png")
    plt.savefig(out, dpi=150)
    plt.close()
    print(f"[grapher] core_stats_summary.png 保存: {out}")


# ─────────────────────────────────────────────
# 2. 単一実験 NUMA アクセス比較
# ─────────────────────────────────────────────
def generate_numa_graph(
    output_dir: str,
    node_stats: dict,
    preset_name: str,
    cpu_map: list,
    num_threads: int,
    workload: str = "CG",
    bench_class: str = "?",
) -> None:
    if not node_stats:
        return

    nodes = list(node_stats.keys())
    reads = [node_stats[n]["reads"] for n in nodes]
    writes = [node_stats[n]["writes"] for n in nodes]
    totals = [reads[i] + writes[i] for i in range(len(nodes))]
    labels = [f"Node {n}\n(CPU {'0-7' if n == 0 else '8-15'})" for n in nodes]

    node_thread_count = {0: 0, 1: 0}
    for t in range(min(num_threads, 16)):
        node_thread_count[0 if cpu_map[t] < 8 else 1] += 1

    colors_read = ["#4C9BE8", "#E87A4C"]
    colors_write = ["#A8C8F0", "#F0BCA8"]

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle(
        f"NUMA Memory Access — {workload.upper()} Class {bench_class}  "
        f"[preset: {preset_name}, {num_threads} threads]",
        fontsize=13,
        fontweight="bold",
    )

    x = range(len(nodes))
    bars_r = axes[0].bar(x, reads, color=colors_read, label="Reads", width=0.5)
    bars_w = axes[0].bar(
        x, writes, color=colors_write, label="Writes", bottom=reads, width=0.5
    )
    axes[0].set_xticks(list(x))
    axes[0].set_xticklabels(labels, fontsize=11)
    axes[0].set_ylabel("Memory Requests", fontsize=11)
    axes[0].set_title("Reads & Writes per Node", fontsize=12)
    axes[0].legend()
    axes[0].yaxis.set_major_formatter(
        plt.FuncFormatter(lambda v, _: f"{int(v):,}")
    )
    for bar, val in zip(bars_r, reads):
        if val > 0:
            axes[0].text(
                bar.get_x() + bar.get_width() / 2,
                val / 2,
                f"{val:,}",
                ha="center",
                va="center",
                fontsize=9,
                color="white",
                fontweight="bold",
            )
    for bar, r_val, w_val in zip(bars_w, reads, writes):
        if w_val > 0:
            axes[0].text(
                bar.get_x() + bar.get_width() / 2,
                r_val + w_val / 2,
                f"{w_val:,}",
                ha="center",
                va="center",
                fontsize=9,
                color="white",
                fontweight="bold",
            )

    grand = sum(totals)
    if grand > 0:
        pie_labels = [
            f"Node {n}\n{totals[n]:,} reqs\n({node_thread_count[n]} threads)"
            for n in nodes
        ]
        axes[1].pie(
            totals,
            labels=pie_labels,
            colors=["#4C9BE8", "#E87A4C"],
            autopct="%1.1f%%",
            startangle=90,
            textprops={"fontsize": 10},
            wedgeprops={"edgecolor": "white", "linewidth": 2},
        )
        axes[1].set_title("Total Access Share per Node", fontsize=12)
    else:
        axes[1].text(0.5, 0.5, "No data", ha="center", va="center")

    mapping_str = (
        "Thread→CPU: "
        + ", ".join(
            f"T{t}→C{cpu_map[t]}(N{0 if cpu_map[t]<8 else 1})"
            for t in range(min(num_threads, 8))
        )
        + (" ..." if num_threads > 8 else "")
    )
    fig.text(0.5, 0.01, mapping_str, ha="center", fontsize=8, color="gray")

    plt.tight_layout(rect=[0, 0.04, 1, 1])
    out = os.path.join(output_dir, "numa_access.png")
    plt.savefig(out, dpi=150)
    plt.close()
    print(f"[grapher] numa_access.png 保存: {out}")
