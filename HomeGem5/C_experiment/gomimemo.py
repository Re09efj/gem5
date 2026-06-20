import m5
import os
from m5.objects import *
from pathlib import Path
import sys
from utility.mover import *

# ============================================================
# 設定
# ============================================================
STRATEGY          = 'Scatter'
CONCENTRATED_NODE = 0
NUM_NODES            = 2
BIG_CORES_PER_NODE   = 4
SMALL_CORES_PER_NODE = 4

BIG_CLOCK   = '4GHz'
SMALL_CLOCK = '1.2GHz'

MEM_PER_NODE   = '1GiB'
MEM_STRIDE     = 0x40000000

L1_SIZE  = '256KiB'
L1_ASSOC = 8
L2_SIZE  = '2MiB'
L2_ASSOC = 8

REMOTE_LATENCY = '100000ns'

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
    return TimingSimpleCPU(
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
# ワークロード割り当て
# ============================================================
binary = '/home/hiragahama/gem5/HomeGem5/binary/matrixopted'
all_cpus = [cpu for node in nodes for cpu in node.cpus]

def make_process(pid, cmd):
    p = Process(pid=pid)
    p.cmd = [cmd]
    return p

def make_dummy(pid):
    p = Process(pid=pid)
    p.cmd = ["/home/hiragahama/gem5/HomeGem5/binary/dummy_exit"]
    return p

if STRATEGY == 'Packed':
    active_cpus = nodes[CONCENTRATED_NODE].cpus
    idle_cpus   = [cpu for i, node in enumerate(nodes)
                   if i != CONCENTRATED_NODE
                   for cpu in node.cpus]
    for idx, cpu in enumerate(active_cpus):
        cpu.workload = make_process(100 + idx, binary)
        cpu.createThreads()
    for idx, cpu in enumerate(idle_cpus):
        cpu.workload = make_dummy(200 + idx)
        cpu.createThreads()

elif STRATEGY == 'Scatter':
    for idx, cpu in enumerate(all_cpus):
        p = Process(pid=100 + idx)
        p.cmd = [binary, str(idx)]  # argv[1]にcpu_idを渡す
        cpu.workload = p
        cpu.createThreads()

elif STRATEGY == 'HPO':
    for idx, cpu in enumerate(all_cpus):
        is_big = (idx % (BIG_CORES_PER_NODE + SMALL_CORES_PER_NODE)) < BIG_CORES_PER_NODE
        cpu.workload = (make_process(100 + idx, binary) if is_big
                        else make_dummy(200 + idx))
        cpu.createThreads()

elif STRATEGY in ('MPO', 'SPO'):
    for idx, cpu in enumerate(all_cpus):
        cpu.workload = make_process(100 + idx, binary)
        cpu.createThreads()

system.workload = SEWorkload.init_compatible(binary)
root = Root(full_system=False, system=system)
m5.instantiate()
m5.simulate()
m5.stats.dump()
move_outputs_to_timestamped_dir(STRATEGY,NUM_NODES,BIG_CORES_PER_NODE,SMALL_CORES_PER_NODE)