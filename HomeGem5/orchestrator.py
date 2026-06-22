import subprocess
from datetime import datetime
import os
from concurrent.futures import ThreadPoolExecutor



gem5 = "/home/hiragahama/gem5/build/X86/gem5.opt"
MYEXP = "/home/hiragahama/gem5/HomeGem5/my_experiment.py"
BINARY = "/home/hiragahama/gem5/HomeGem5/binary/NPB3.4.4/NPB3.4-OMP/bin/mg.S.numa_firsttouch.x"
BASE_OUTPUT_DIR="/home/hiragahama/gem5/HomeGem5/Outputs"

def run(strategy, num_threads, binary=BINARY, num_nodes=2):
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = os.path.join(BASE_OUTPUT_DIR, f"{strategy}_{num_threads}TH_{now}")
    os.makedirs(output_dir, exist_ok=True)
    subprocess.run(
        [
            gem5,
            "-d",
            output_dir,
            # "--debug-flags=TLB",
            MYEXP,
            f"--strategy={strategy}",
            f"--num-threads={num_threads}",
            f"--binary={binary}",
            f"--num-nodes={num_nodes}",
        ]
    )


def main():
    tasks = [
        ("Scatter", 4),
        ("MPO",     4),
        ("HPO",     4),
        ("Packed",  4)
    ]
    
    print(f"[*] {len(tasks)}のシミュレーションを同時に並列実行します...")
    
    with ThreadPoolExecutor(max_workers=len(tasks)) as executor:
        futures = [executor.submit(run, *task) for task in tasks]
        for future in futures:
            future.result() 

    print("[*] すべてのシミュレーションの並列実行が完了しました。")
main()