import os
import shutil
from datetime import datetime
import shutil
from utility.reformer import text_to_csv

DEFAULT_M5OUT = os.path.join(os.getcwd(), "m5out")
# 最終的に成果物をまとめたいベースディレクトリ
BASE_OUTPUT_DIR = os.path.expanduser("/home/hiragahama/gem5/HomeGem5/Outputs")

def get_default_m5out():
    """gem5に渡すためのデフォルトの出力パスを返します"""
    return DEFAULT_M5OUT

def move_outputs_to_timestamped_dir(STRATEGY,NUM_THREADS):
    # 時刻を取得して一意のフォルダ名を決定
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    final_output_dir = os.path.join(BASE_OUTPUT_DIR, f"{STRATEGY}_{NUM_THREADS}THDS_{now}")
    
    # 移動させたいターゲットファイル群
    target_files = ["stats.txt", "config.ini", "config.json","experiment_config.txt"]
    
    # 実際に生成されているファイルだけを抽出
    files_to_move = [f for f in target_files if os.path.exists(os.path.join(DEFAULT_M5OUT, f))]
    
    if files_to_move:
        # 成果物が存在するこのタイミングで初めてフォルダを新規作成
        os.makedirs(final_output_dir, exist_ok=True)
        # print(f"[*] [Mover] Created destination: {final_output_dir}")
        
        for file_name in files_to_move:
            src_path = os.path.join(DEFAULT_M5OUT, file_name)
            dst_path = os.path.join(final_output_dir, file_name)
            
            # 切り取り移動を実行
            shutil.move(src_path, dst_path)
            # print(f"  [Moved] {file_name} -> {final_output_dir}")
            
        print(f"\n[+] [Mover] All tasks done! Saved in: {final_output_dir}\n")
        shutil.rmtree(DEFAULT_M5OUT)
        text_to_csv(os.path.join(final_output_dir, "stats.txt"))

    else:
        print("\n[!] [Mover] No output files found to move. Simulation may have failed.\n")