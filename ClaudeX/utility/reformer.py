"""
reformer.py
gem5 stats.txt を pandas DataFrame に変換して CSV として保存する。
gem5 stats.txt を CSV に変換する。
"""

import os
import pandas as pd


def text_to_csv(stats_file_path: str) -> str | None:
    stats_data = []

    with open(stats_file_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if "#" in line:
                data_part, description = line.split("#", 1)
                description = description.strip()
            else:
                data_part  = line
                description = ""

            parts = data_part.split()
            if len(parts) >= 2:
                stat_name = parts[0]
                if stat_name.startswith("---"):
                    continue
                value_str = parts[1]
                try:
                    value = int(value_str) if "." not in value_str else float(value_str)
                except ValueError:
                    value = value_str

                stats_data.append({
                    "stat_name":   stat_name,
                    "value":       value,
                    "description": description,
                })

    if not stats_data:
        print("[reformer] 警告: データが1件も取得できませんでした。")
        return None

    df = pd.DataFrame(stats_data)
    output_path = os.path.join(os.path.dirname(stats_file_path), "stats.csv")
    df.to_csv(output_path, index=False)
    print(f"[reformer] CSV 保存: {output_path}")
    return output_path
