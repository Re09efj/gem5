import json
import os
import re

from utility.mover import *

import m5
from m5.objects import *

# ============================================================
# デフォルト設定
# ============================================================
BINARY_PATH = "/home/hiragahama/gem5/HomeGem5/binary/matrix"
STRATEGY = "Scatter"
CONCENTRATED_NODE = 0
NUM_NODES = 2
BIG_CORES_PER_NODE = 4
SMALL_CORES_PER_NODE = 4
NUM_THREADS = 2
BIG_CLOCK = "4GHz"
SMALL_CLOCK = "1GHz"
MEM_PER_NODE = "1GiB"
MEM_STRIDE = 0x40000000
L1_SIZE = "256KiB"
L1_ASSOC = 8
L2_SIZE = "2MiB"
L2_ASSOC = 8
REMOTE_LATENCY = "1ns"
DUMMY = "/home/hiragahama/gem5/HomeGem5/binary/tiny_exit"

# ============================================================
# コマンドライン引数（masterからの指定で上書き）
# ============================================================
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--strategy", type=str, default="Scatter")
parser.add_argument("--num-threads", type=int, default=2)
parser.add_argument("--binary", type=str, default=BINARY_PATH)
parser.add_argument("--num-nodes", type=int, default=NUM_NODES)
args = parser.parse_args(sys.argv[1:])

STRATEGY = args.strategy
NUM_THREADS = args.num_threads
BINARY_PATH = args.binary
NUM_NODES = args.num_nodes

CORES_PER_NODE = BIG_CORES_PER_NODE + SMALL_CORES_PER_NODE


# ============================================================
# キャッシュ定義
# ============================================================
class L1ICache(Cache):
    size = L1_SIZE
    assoc = L1_ASSOC
    tag_latency = 1
    data_latency = 1
    response_latency = 1
    mshrs = 4
    tgts_per_mshr = 20


class L1DCache(Cache):
    size = L1_SIZE
    assoc = L1_ASSOC
    tag_latency = 1
    data_latency = 1
    response_latency = 1
    mshrs = 4
    tgts_per_mshr = 20


class L2Cache(Cache):
    size = L2_SIZE
    assoc = L2_ASSOC
    tag_latency = 5
    data_latency = 5
    response_latency = 5
    mshrs = 16
    tgts_per_mshr = 20


# ============================================================
# ヘルパー関数
# ============================================================
def make_cpu(cpu_id, clock):
    return X86O3CPU(
        cpu_id=cpu_id,
        clk_domain=SrcClockDomain(clock=clock, voltage_domain=VoltageDomain()),
    )


def connect_cpu_to_xbar(cpu, xbar):
    cpu.createInterruptController()
    cpu.interrupts[0].pio = xbar.mem_side_ports
    cpu.interrupts[0].int_requestor = xbar.cpu_side_ports
    cpu.interrupts[0].int_responder = xbar.mem_side_ports

    cpu.icache = L1ICache()
    cpu.dcache = L1DCache()
    cpu.icache.cpu_side = cpu.icache_port
    cpu.dcache.cpu_side = cpu.dcache_port

    cpu.l2cache = L2Cache()
    cpu.l2bus = L2XBar()
    cpu.icache.mem_side = cpu.l2bus.cpu_side_ports
    cpu.dcache.mem_side = cpu.l2bus.cpu_side_ports
    cpu.l2bus.mem_side_ports = cpu.l2cache.cpu_side
    cpu.l2cache.mem_side = xbar.cpu_side_ports

    cpu.mmu.dtb.walker.port = xbar.cpu_side_ports
    cpu.mmu.itb.walker.port = xbar.cpu_side_ports


def build_node(node_id, cpu_global_id):
    node = SubSystem()
    big_cpus = [
        make_cpu(cpu_global_id + j, BIG_CLOCK)
        for j in range(BIG_CORES_PER_NODE)
    ]
    small_cpus = [
        make_cpu(cpu_global_id + BIG_CORES_PER_NODE + j, SMALL_CLOCK)
        for j in range(SMALL_CORES_PER_NODE)
    ]
    node.cpus = big_cpus + small_cpus

    node.xbar = SystemXBar()
    node.mem_ctrl = MemCtrl()
    node.mem_ctrl.dram = DDR3_1600_8x8(
        range=AddrRange(start=node_id * MEM_STRIDE, size=MEM_PER_NODE),
        ranks_per_channel=1,
    )
    node.mem_ctrl.port = node.xbar.mem_side_ports

    for cpu in node.cpus:
        connect_cpu_to_xbar(cpu, node.xbar)

    return node


def connect_nodes_with_bridges(system, nodes):
    bridge_idx = 0
    for i in range(NUM_NODES):
        for j in range(NUM_NODES):
            if i == j:
                continue
            bridge = Bridge(
                delay=REMOTE_LATENCY,
                ranges=[AddrRange(start=j * MEM_STRIDE, size=MEM_PER_NODE)],
                req_size=32,
                resp_size=32,
            )
            bridge.cpu_side_port = nodes[i].xbar.mem_side_ports
            bridge.mem_side_port = nodes[j].xbar.cpu_side_ports
            setattr(system, f"bridge{bridge_idx}", bridge)
            bridge_idx += 1


def compute_active_indices(strategy, num_threads):
    if strategy == "Packed":
        return list(range(CORES_PER_NODE))[:num_threads]

    elif strategy == "Scatter":
        indices = []
        for i in range(num_threads // 2):
            indices.append(i)
            indices.append(i + CORES_PER_NODE)
        return indices[:num_threads]

    elif strategy == "HPO":
        big_node0 = list(range(0, BIG_CORES_PER_NODE))
        big_node1 = list(
            range(CORES_PER_NODE, CORES_PER_NODE + BIG_CORES_PER_NODE)
        )
        small_node0 = list(range(BIG_CORES_PER_NODE, CORES_PER_NODE))
        small_node1 = list(
            range(CORES_PER_NODE + BIG_CORES_PER_NODE, 2 * CORES_PER_NODE)
        )
        return (big_node0 + big_node1 + small_node0 + small_node1)[
            :num_threads
        ]

    elif strategy == "MPO":
        return [0, 1, 8, 9, 2, 3, 10, 11, 4, 5, 12, 13, 6, 7, 14, 15][
            :num_threads
        ]

    else:
        raise ValueError(f"Unknown STRATEGY: {strategy}")


def assign_workloads(all_cpus, omp_proc):
    all_cpus[0].workload = omp_proc
    all_cpus[0].createThreads()

    dummy_pid = 200
    for cpu in all_cpus[1:]:
        dummy = Process(pid=dummy_pid)
        dummy.cmd = [DUMMY]
        cpu.workload = dummy
        cpu.createThreads()
        dummy_pid += 1


def save_config(path):
    """実験条件をm5out/に保存（move_outputs_to_timestamped_dirで一緒に移動される）"""
    with open(path, "w") as f:
        f.write(f"STRATEGY={STRATEGY}\n")
        f.write(f"NUM_THREADS={NUM_THREADS}\n")
        f.write(f"NUM_NODES={NUM_NODES}\n")
        f.write(f"BIG_CORES_PER_NODE={BIG_CORES_PER_NODE}\n")
        f.write(f"SMALL_CORES_PER_NODE={SMALL_CORES_PER_NODE}\n")
        f.write(f"BIG_CLOCK={BIG_CLOCK}\n")
        f.write(f"SMALL_CLOCK={SMALL_CLOCK}\n")
        f.write(f"MEM_PER_NODE={MEM_PER_NODE}\n")
        f.write(f"REMOTE_LATENCY={REMOTE_LATENCY}\n")
        f.write(f"L1_SIZE={L1_SIZE}\n")
        f.write(f"L2_SIZE={L2_SIZE}\n")
        f.write(f"BINARY_PATH={BINARY_PATH}\n")
        f.write(f"active_indices={active_indices}\n")


def read_node_stats(stats_file, num_nodes):
    with open(stats_file) as f:
        content = f.read()
    for i in range(num_nodes):
        node = f"node{i}"
        reads = re.search(
            rf"system\.{node}\.mem_ctrl\.readReqs\s+(\d+)", content
        )
        writes = re.search(
            rf"system\.{node}\.mem_ctrl\.writeReqs\s+(\d+)", content
        )
        print(
            f"{node}: reads={reads.group(1) if reads else 0}, "
            f"writes={writes.group(1) if writes else 0}"
        )


# ============================================================
# メイン
# ============================================================
active_indices = compute_active_indices(STRATEGY, NUM_THREADS)
affinity_order = ",".join(map(str, active_indices))

print(f"STRATEGY: {STRATEGY}")
print(f"num_threads: {NUM_THREADS}")
print(f"active_indices: {active_indices}")
print(f"binary: {BINARY_PATH}")
print(f"binary exists: {os.path.exists(BINARY_PATH)}")
print(f"DUMMY exists: {os.path.exists(DUMMY)}")

# --- システム構築 ---
system = System()
system.clk_domain = SrcClockDomain(
    clock="1GHz", voltage_domain=VoltageDomain()
)
system.mem_mode = "timing"
system.mem_ranges = [
    AddrRange(start=i * MEM_STRIDE, size=MEM_PER_NODE)
    for i in range(NUM_NODES)
]

nodes = []
cpu_global_id = 0
for i in range(NUM_NODES):
    node = build_node(i, cpu_global_id)
    cpu_global_id += CORES_PER_NODE
    nodes.append(node)
    setattr(system, f"node{i}", node)

connect_nodes_with_bridges(system, nodes)
system.system_port = nodes[0].xbar.cpu_side_ports

print(f"total CPUs: {sum(len(n.cpus) for n in nodes)}")

# --- ワークロード定義 ---
omp_proc = Process(pid=100)
omp_proc.cmd = [BINARY_PATH]
omp_proc.env = [
    f"GOMP_CPU_AFFINITY={affinity_order}",
    f"OMP_NUM_THREADS={NUM_THREADS}",
    f"GEM5_TARGET_CPUS={','.join(map(str, active_indices[1:]))}",
    "OMP_DYNAMIC=FALSE",
    "GOMP_SPINCOUNT=100000000",
]

all_cpus = [cpu for node in nodes for cpu in node.cpus]
assign_workloads(all_cpus, omp_proc)

system.workload = SEWorkload.init_compatible(BINARY_PATH)
root = Root(full_system=False, system=system)

# --- シミュレーション実行 ---
m5.instantiate()
MMAP_START = 0x7FFFF76FB000
MMAP_END = 0x7FFFF7FFEFFF
MMAP_SIZE = MMAP_END - MMAP_START + 1
HALF = MMAP_SIZE // 2

m5.simulate()
m5.stats.dump()

# --- 結果表示・保存 ---
read_node_stats("m5out/stats.txt", NUM_NODES)
save_config("m5out/experiment_config.txt")
move_outputs_to_timestamped_dir(STRATEGY, NUM_THREADS)
