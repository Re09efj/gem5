from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.components.processors.cpu_types import CPUTypes
from gem5.components.memory import DualChannelDDR4_2400
from gem5.components.cachehierarchies.classic.private_l1_private_l2_cache_hierarchy import PrivateL1PrivateL2CacheHierarchy
from gem5.isas import ISA
from gem5.simulate.simulator import Simulator
from gem5.resources.resource import BinaryResource
import argparse
import os

parser = argparse.ArgumentParser(description="Hetero NUMA with Rich Statistics")
parser.add_argument("--cmd", type=str, default="/bin/echo")
parser.add_argument("--options", type=str, default="Stats Test")
parser.add_argument("--num-cores", type=int, default=24)
args = parser.parse_args()

print(f"Running: {args.cmd} {args.options} with {args.num_cores} cores")

processor = SimpleProcessor(
    cpu_type=CPUTypes.O3,
    num_cores=args.num_cores,
    isa=ISA.X86,
)

memory = DualChannelDDR4_2400(size="16GB")

board = SimpleBoard(
    clk_freq="3GHz",
    processor=processor,
    memory=memory,
    cache_hierarchy=PrivateL1PrivateL2CacheHierarchy(
        l1d_size="32kB", l1i_size="32kB", l2_size="256kB"
    ),
)

# ワークロード設定
board.set_se_binary_workload(
    BinaryResource(local_path=args.cmd),
    arguments=[args.options] if args.options else []
)

# 統計出力設定（研究用に強化）
board._options = type('obj', (object,), {
    'stats_file': 'stats.txt',
    'json_stats': 'stats.json'
})()

sim = Simulator(board=board)
print("Simulation running... (Statistics will be rich)")
sim.run()

print("\n=== Simulation Completed ===")
print(f"Stats file: m5out/stats.txt")
print(f"JSON stats: m5out/stats.json")
