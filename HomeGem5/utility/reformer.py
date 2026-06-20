import os
import pandas as pd
import time

def text_to_csv(stats_file_path):
    stats_data = []
    
    with open(stats_file_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            line = line.strip()
            
            # 1. シャープ（#）があれば、そこで「データ部分」と「コメント部分」に分割する
            if "#" in line:
                data_part, description = line.split("#", 1)
                description = description.strip() # 最初の半角スペースや前後の空白を無視
            else:
                data_part = line
                description = ""
                
            # 2. データ部分から「最初の文字（統計名）」と「次の数字（値）」を取り出す
            # split() は、空白・タブがどれだけ連続して挟まっていても、自動でそれらを無視して綺麗に切り分けてくれます
            parts = data_part.split()
            
            # 正しく「文字」と「数字」が取得できた行だけを処理（ヘッダー行などは自動で弾かれます）
            if len(parts) >= 2:
                stat_name = parts[0]
                if stat_name.startswith('---'):
                    continue
                value_str = parts[1]
                
                # 値を int か float に変換（変換できない特殊な文字列はそのまま保持）
                try:
                    value = int(value_str) if '.' not in value_str else float(value_str)
                except ValueError:
                    value = value_str
                
                # 3. データを格納
                stats_data.append({
                    "stat_name": stat_name,
                    "value": value,
                    "description": description
                })
    if not stats_data:
        print("⚠️ 警告: データが1件も取得できませんでした。")
        return

    df = pd.DataFrame(stats_data)
    output_path = os.path.join(os.path.dirname(stats_file_path), "stats.csv")
    
    df.to_csv(output_path, index=False)
    try:
        from utility.grapher import generate_core_stats_graph
        generate_core_stats_graph(output_path)
    except Exception as e:
        print(f"⚠️ グラフ生成中にエラーが発生しました: {e}")