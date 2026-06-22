"""
config_writer.py
実験条件を affinity_config.txt として出力ディレクトリに保存する。
"""

import os


def save_affinity_config(
    output_dir: str,
    preset_name: str,
    workload: str,
    bench_class: str,
    cpu_map: list,
    num_threads: int,
    num_nodes: int = 2,
    big_cpn: int = 4,
    sml_cpn: int = 4,
) -> None:
    path = os.path.join(output_dir, "affinity_config.txt")
    lines = [
        f"BENCHMARK={workload.upper()}.{bench_class} (NPB3.4.4 OpenMP)",
        f"PRESET={preset_name}",
        f"NUM_THREADS={num_threads}",
        f"NUM_NODES={num_nodes}",
        f"BIG_CORES_PER_NODE={big_cpn}",
        f"SMALL_CORES_PER_NODE={sml_cpn}",
        f"cpu_map={cpu_map}",
        "",
        "# Thread -> CPU -> Node mapping",
    ]
    for t in range(min(num_threads, 16)):
        cpu = cpu_map[t]
        node = 0 if cpu < 8 else 1
        ctype = "P" if (cpu % 8) < 4 else "E"
        lines.append(
            f"  thread{t:02d} -> CPU{cpu:02d} (Node{node} {ctype}-core)"
        )

    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"[config] 保存: {path}")
