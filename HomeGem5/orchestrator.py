import subprocess

gem5 = "/home/hiragahama/gem5/build/X86/gem5.opt"
MYEXP = "/home/hiragahama/gem5/HomeGem5/my_experiment.py"
BINARY = "/home/hiragahama/gem5/HomeGem5/binary/NPB3.4.4/NPB3.4-OMP/bin/mg.S.x"


def run(strategy, num_threads, binary=BINARY, num_nodes=2):
    subprocess.run(
        [
            gem5,
            MYEXP,
            f"--strategy={strategy}",
            f"--num-threads={num_threads}",
            f"--binary={binary}",
            f"--num-nodes={num_nodes}",
        ]
    )


def main():
    run("Scatter", 4)
    # run("MPO",     1)
    # run("HPO",     1)
    # run("Packed",  1)


main()
