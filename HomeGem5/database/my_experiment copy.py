import m5
import os
from m5.objects import *
from pathlib import Path
import sys
import json
from utility.rawTxtReader import *

# ============================================================
# 設定
# ============================================================

BINARY_PATH = '/home/hiragahama/gem5/HomeGem5/binary/matrix'
STRATEGY          = 'Scatter'
CONCENTRATED_NODE = 0
NUM_NODES            = 2
BIG_CORES_PER_NODE   = 4
SMALL_CORES_PER_NODE = 4
NUM_THREADS= 0
BIG_CLOCK   = '4GHz'
SMALL_CLOCK = '1GHz'
MEM_PER_NODE   = '1GiB'
MEM_STRIDE     = 0x40000000
L1_SIZE  = '256KiB'
L1_ASSOC = 8
L2_SIZE  = '2MiB'
L2_ASSOC = 8
REMOTE_LATENCY = '1000ns'

numaconfig = '/home/hiragahama/gem5/HomeGem5/database/numaconfig.json'
# 💡 JSONを読み込んで、グローバル変数として一括展開する
with open(numaconfig, 'r') as f:
    config_data = json.load(f)
    for key, value in config_data.items():
        globals()[key] = value

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

system = System()
system.clk_domain = SrcClockDomain(
    clock='1GHz',
    voltage_domain=VoltageDomain()
)
system.mem_mode = 'timing'
system.mem_ranges = [AddrRange(start=i * MEM_STRIDE, size=MEM_PER_NODE)
                     for i in range(NUM_NODES)]

def make_cpu(cpu_id, clock):
    return X86O3CPU(
        cpu_id=cpu_id,
        clk_domain=SrcClockDomain(clock=clock, voltage_domain=VoltageDomain())
    )

nodes = []
cpu_global_id = 0

for i in range(NUM_NODES):
    node = SubSystem()

    big_cpus = [make_cpu(cpu_global_id + j, BIG_CLOCK)
                for j in range(BIG_CORES_PER_NODE)]
    cpu_global_id += BIG_CORES_PER_NODE

    small_cpus = [make_cpu(cpu_global_id + j, SMALL_CLOCK)
                  for j in range(SMALL_CORES_PER_NODE)]
    cpu_global_id += SMALL_CORES_PER_NODE

    node.cpus = big_cpus + small_cpus

    # ノード内XBar
    node.xbar = SystemXBar()

    # ローカルメモリ
    node.mem_ctrl = MemCtrl()
    node.mem_ctrl.dram = DDR3_1600_8x8(
        range=AddrRange(start=i * MEM_STRIDE, size=MEM_PER_NODE),
        ranks_per_channel=1,
    )
    node.mem_ctrl.port = node.xbar.mem_side_ports

    # CPUをnode.xbarに接続
    for cpu in node.cpus:
        cpu.createInterruptController()
        cpu.interrupts[0].pio           = node.xbar.mem_side_ports
        cpu.interrupts[0].int_requestor = node.xbar.cpu_side_ports
        cpu.interrupts[0].int_responder = node.xbar.mem_side_ports

        cpu.icache = L1ICache()
        cpu.dcache = L1DCache()
        cpu.icache.cpu_side = cpu.icache_port
        cpu.dcache.cpu_side = cpu.dcache_port

        cpu.l2cache = L2Cache()
        cpu.l2bus   = L2XBar()
        cpu.icache.mem_side      = cpu.l2bus.cpu_side_ports
        cpu.dcache.mem_side      = cpu.l2bus.cpu_side_ports
        cpu.l2bus.mem_side_ports = cpu.l2cache.cpu_side
        cpu.l2cache.mem_side     = node.xbar.cpu_side_ports

        cpu.mmu.dtb.walker.port = node.xbar.cpu_side_ports
        cpu.mmu.itb.walker.port = node.xbar.cpu_side_ports

    nodes.append(node)
    setattr(system, f'node{i}', node)

# ============================================================
# ノード間をBridgeで接続
# 公式gem5コードと同じパターン:
# self.iobridge = Bridge(delay='50ns') のように個別名で登録
# 参考: github.com/uart/gem5-mirror/blob/master/configs/example/arm/devices.py
# ============================================================
bridge_idx = 0
for i in range(NUM_NODES):
    for j in range(NUM_NODES):
        if i == j:
            continue
        bridge = Bridge(
            delay=REMOTE_LATENCY,
            ranges=[AddrRange(start=j * MEM_STRIDE, size=MEM_PER_NODE)]
        )
        bridge.cpu_side_port = nodes[i].xbar.mem_side_ports
        bridge.mem_side_port = nodes[j].xbar.cpu_side_ports
        # リストではなく個別名でsystemに登録（gem5の公式パターン）
        setattr(system, f'bridge{bridge_idx}', bridge)
        bridge_idx += 1

system.system_port = nodes[0].xbar.cpu_side_ports

# ============================================================
# ワークロード割り当て（OpenMPI SE mode 対応版）
# ============================================================
binary = BINARY_PATH
DUMMY  = "/home/hiragahama/gem5/HomeGem5/binary/dummy_exit"

all_cpus = [cpu for node in nodes for cpu in node.cpus]

# ------------------------------------------------------------
# CPU配置戦略
# ------------------------------------------------------------

if STRATEGY == "Packed":
    cpu_order = list(range(len(all_cpus)))

elif STRATEGY == "Scatter":
    cpu_order = [0,8,1,9,2,10,3,11,4,12,5,13,6,14,7,15]

elif STRATEGY == "HPO":
    cpu_order = [0,1,2,3,8,9,10,11,4,5,6,7,12,13,14,15]

elif STRATEGY == "MPO":
    cpu_order = [
        0,1,8,9,
        2,3,10,11,
        4,5,12,13,
        6,7,14,15
    ]

else:
    raise ValueError(f"Unknown STRATEGY: {STRATEGY}")

# OpenMPで実際に使うCPU
active_cpu_ids = set(cpu_order[:NUM_THREADS])

# ------------------------------------------------------------
# OpenMPプロセス
# ------------------------------------------------------------

omp_proc = Process()
omp_proc.cmd = [binary]
omp_proc.env = [f"OMP_NUM_THREADS={NUM_THREADS}"]

# ------------------------------------------------------------
# CPUへ割り当て
# ------------------------------------------------------------
for idx, cpu in enumerate(all_cpus):

    if idx in active_cpu_ids:
        cpu.workload = omp_proc

    else:
        dummy = Process()
        dummy.cmd = [DUMMY]
        dummy.pid = 1000 + idx
        cpu.workload = dummy

    cpu.createThreads()
# ------------------------------------------------------------
# System workload
# ------------------------------------------------------------

system.workload = SEWorkload.init_compatible(binary)

root = Root(full_system=False, system=system)


# binary = BINARY_PATH

# all_cpus = [cpu for node in nodes for cpu in node.cpus]

# proc = Process()
# proc.cmd = [binary]
# OMP_NUM_THREADS="OMP_NUM_THREADS="+str(NUM_THREADS)
# proc.env = [OMP_NUM_THREADS]

# for cpu in all_cpus:
#     cpu.workload = proc
#     cpu.createThreads()

# system.workload = SEWorkload.init_compatible(binary)
# root = Root(full_system=False, system=system)
m5.instantiate()
m5.simulate()
m5.stats.dump()
move_outputs_to_timestamped_dir(STRATEGY,NUM_NODES,BIG_CORES_PER_NODE,SMALL_CORES_PER_NODE)