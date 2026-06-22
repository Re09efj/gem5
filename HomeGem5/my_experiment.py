import json
import os
import re
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
parser.add_argument("--output-path", type=str)
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


def connect_cpu_to_membus(cpu, membus):
    """CPUを単一のコヒーレントなmembusに接続する。
    membusがsnoopを全CPUに伝播するため、ノードをまたいでも
    キャッシュコヒーレンシ(MESI)が機能し、OpenMPバリアが正しく動作する。
    """
    cpu.createInterruptController()
    cpu.interrupts[0].pio = membus.mem_side_ports
    cpu.interrupts[0].int_requestor = membus.cpu_side_ports
    cpu.interrupts[0].int_responder = membus.mem_side_ports

    cpu.icache = L1ICache()
    cpu.dcache = L1DCache()
    cpu.icache.cpu_side = cpu.icache_port
    cpu.dcache.cpu_side = cpu.dcache_port

    cpu.l2cache = L2Cache()
    cpu.l2bus = L2XBar()
    cpu.icache.mem_side = cpu.l2bus.cpu_side_ports
    cpu.dcache.mem_side = cpu.l2bus.cpu_side_ports
    cpu.l2bus.mem_side_ports = cpu.l2cache.cpu_side
    cpu.l2cache.mem_side = membus.cpu_side_ports

    cpu.mmu.dtb.walker.port = membus.cpu_side_ports
    cpu.mmu.itb.walker.port = membus.cpu_side_ports


def make_cpus(node_id, cpu_global_id):
    """1ノード分のCPU群を生成して返す（接続はまだしない）"""
    big_cpus = [
        make_cpu(cpu_global_id + j, BIG_CLOCK)
        for j in range(BIG_CORES_PER_NODE)
    ]
    small_cpus = [
        make_cpu(cpu_global_id + BIG_CORES_PER_NODE + j, SMALL_CLOCK)
        for j in range(SMALL_CORES_PER_NODE)
    ]
    return big_cpus + small_cpus


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

    elif strategy == "SPO":
        # スケジューリング優先度協調制御（暫定: Scatter と同じ配置）
        indices = []
        for i in range(num_threads // 2):
            indices.append(i)
            indices.append(i + CORES_PER_NODE)
        return indices[:num_threads]

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


def read_mem_stats(stats_file, num_nodes):
    """単一membus構成では mem_ctrl の名前が変わるので、
    両ノードのmem_ctrlを名前で拾って表示する。"""
    # with open(stats_file) as f:
    #     content = f.read()
    # for i in range(num_nodes):
    #     name = f"mem_ctrl{i}"
    #     reads = re.search(rf"system\.{name}\.readReqs\s+(\d+)", content)
    #     writes = re.search(rf"system\.{name}\.writeReqs\s+(\d+)", content)
    #     print(
    #         f"node{i} ({name}): reads={reads.group(1) if reads else 0}, "
    #         f"writes={writes.group(1) if writes else 0}"
    #     )


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

# 単一のコヒーレントなfabric（membus）。
# 全CPUのL2とすべてのメモリコントローラをここに集約することで、
# ノードをまたいでもMESIプロトコルが機能する（バリアが動く）。
system.membus = SystemXBar()

# 全ノードのCPUを生成し、まとめてmembusに接続
all_cpus = []
cpu_global_id = 0
for i in range(NUM_NODES):
    cpus = make_cpus(i, cpu_global_id)
    cpu_global_id += CORES_PER_NODE
    all_cpus.extend(cpus)
setattr(system, "cpus", all_cpus)

for cpu in all_cpus:
    connect_cpu_to_membus(cpu, system.membus)

# 各ノードのメモリコントローラをmembusに接続。
# range で物理アドレス空間を分割し、どのアドレスがどのノードに
# 属するかを表現する（NUMAのアドレスマップ）。
mem_ctrls = []
for i in range(NUM_NODES):
    mc = MemCtrl()
    mc.dram = DDR3_1600_8x8(
        range=AddrRange(start=i * MEM_STRIDE, size=MEM_PER_NODE),
        ranks_per_channel=1,
    )
    mc.port = system.membus.mem_side_ports
    setattr(system, f"mem_ctrl{i}", mc)
    mem_ctrls.append(mc)

system.system_port = system.membus.cpu_side_ports

print(f"total CPUs: {len(all_cpus)}")

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

assign_workloads(all_cpus, omp_proc)

system.workload = SEWorkload.init_compatible(BINARY_PATH)
root = Root(full_system=False, system=system)

# --- シミュレーション実行 ---
m5.instantiate()

m5.simulate()
m5.stats.dump()

# --- 結果表示・保存 ---
from utility.rawTxtReader import rawTxtReader
from utility.reformer import text_to_csv
from utility.grapher import generate_core_stats_graph
rawTxtReader(os.path.join(m5.options.outdir,"stats.txt"),NUM_NODES)
save_config("experiment_config.txt")
csv_path = text_to_csv(os.path.join(m5.options.outdir,"stats.txt"))
generate_core_stats_graph(csv_path,NUM_NODES,BIG_CORES_PER_NODE,SMALL_CORES_PER_NODE)
