import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def generate_core_stats_graph(csv_path, nn, bcpn, scpn):
    print("[*] Generating graph from CSV...")
    print(csv_path)
    df = pd.read_csv(csv_path)

    if not os.path.exists(csv_path):
        print(f"❌ [Grapher Error] CSVファイルが見つかりません: {csv_path}")
        return

    df = pd.read_csv(csv_path)

    NUM_NODES = nn
    CORES_PER_NODE = bcpn + scpn
    BIG_CORES_PER_NODE = bcpn

    cpi_data = []
    cycles_data = []

    for node_id in range(NUM_NODES):
        for cpu_id in range(CORES_PER_NODE):
            label = f"N{node_id}-{'Big' if cpu_id < BIG_CORES_PER_NODE else 'Small'}{cpu_id}"
            # stat_base = f"system.node{node_id}.cpus{cpu_id}"
            stat_base = f"system.cpus{cpu_id}"
            cpi_row = df[df["stat_name"] == f"{stat_base}.cpi"]
            if not cpi_row.empty:
                cpi_data.append(
                    {
                        "Core": label,
                        "CPI": float(cpi_row.iloc[0]["value"]),
                        "NodeID": node_id,
                        "CoreType": (
                            "Big" if cpu_id < BIG_CORES_PER_NODE else "Small"
                        ),
                    }
                )

            cycles_row = df[df["stat_name"] == f"{stat_base}.numCycles"]
            if not cycles_row.empty:
                cycles_data.append(
                    {
                        "Core": label,
                        "NumCycles": int(cycles_row.iloc[0]["value"]),
                        "NodeID": node_id,
                        "CoreType": (
                            "Big" if cpu_id < BIG_CORES_PER_NODE else "Small"
                        ),
                    }
                )

    df_cpi = pd.DataFrame(cpi_data)
    df_cycles = pd.DataFrame(cycles_data)

    if df_cpi.empty or df_cycles.empty:
        print(
            "⚠️ 警告: グラフに必要なCPUデータ(cpi/numCycles)が見つかりませんでした。"
        )
        return

    # Big/Smallでバーの色を変える palette
    type_palette = {"Big": "steelblue", "Small": "tomato"}

    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(1, 2, figsize=(18, 6))

    # 左：CPI
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

    # 右：NumCycles
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

    output_graph_path = os.path.join(
        os.path.dirname(csv_path), "core_stats_summary.png"
    )
    plt.savefig(output_graph_path, dpi=150)
    plt.close()

    print(f"✨ グラフの自動生成に成功しました！")
