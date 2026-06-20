import json
import subprocess

gem5= '/home/hiragahama/gem5/build/X86/gem5.opt'
numaconfigpath = '/home/hiragahama/gem5/HomeGem5/database/numaconfig.json'
BINARY_PATH="/home/hiragahama/gem5/HomeGem5/binary/NPB3.4.4/NPB3.4-OMP/bin/mg.S.x"
MYEXP='/home/hiragahama/gem5/HomeGem5/my_experiment.py'
OUTPATH="/home/hiragahama/gem5/HomeGem5/Outputs"

def main():
    with open(numaconfigpath, 'r') as f:
        config = json.load(f)
        config["BINARY_PATH"]=BINARY_PATH
        config['STRATEGY'] = 'Scatter'
        config['NUM_NODES'] = 2
        config["NUM_THREADS"] = 4
    with open(numaconfigpath, 'w') as f:
        json.dump(config, f, indent=4)
    result = subprocess.run([gem5, MYEXP])

main()