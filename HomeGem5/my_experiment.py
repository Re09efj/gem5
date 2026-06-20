import m5
import os
from m5.objects import *
from pathlib import Path
import sys
import json
from utility.mover import *

# ============================================================
# 設定
# ============================================================

BINARY_PATH = '/home/hiragahama/gem5/HomeGem5/binary/matrix'
STRATEGY          = 'Scatter'
CONCENTRATED_NODE = 0
NUM_NODES            = 2
BIG_CORES_PER_NODE   = 4
SMALL_CORES_PER_NODE = 4
NUM_THREADS= 2
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
DUMMY="/home/hiragahama/gem5/HomeGem5/binary/dummy_exit"
# ============================================================
# ワークロード割り当て（トポロジベース戦略）
# ============================================================

all_cpus = [cpu for node in nodes for cpu in node.cpus]
num_threads = NUM_THREADS if NUM_THREADS > 0 else len(all_cpus)

print(f"STRATEGY: {STRATEGY}")
print(f"num_threads: {num_threads}")


# --- 1. 戦略に応じた OpenMP のピン留め順（アフィニティ）の定義 ---
if STRATEGY == "Packed":
    active_indices = list(range(0, BIG_CORES_PER_NODE + SMALL_CORES_PER_NODE))
elif STRATEGY == "Scatter":
    active_indices = []
    for i in range(num_threads // 2):
        active_indices.append(i)
        active_indices.append(i + (BIG_CORES_PER_NODE + SMALL_CORES_PER_NODE))
    active_indices = active_indices[:num_threads]
elif STRATEGY == "HPO":
    big_node0   = list(range(0, BIG_CORES_PER_NODE))
    big_node1   = list(range(8, 8 + BIG_CORES_PER_NODE))
    small_node0 = list(range(4, 4 + SMALL_CORES_PER_NODE))
    small_node1 = list(range(12, 12 + SMALL_CORES_PER_NODE))
    active_indices = (big_node0 + big_node1 + small_node0 + small_node1)[:num_threads]
elif STRATEGY == "MPO":
    active_indices = [0,1,8,9, 2,3,10,11, 4,5,12,13, 6,7,14,15][:num_threads]

print(f"active_indices: {active_indices}")
affinity_order = ",".join(map(str, active_indices))

# --- 2. 真のマスタープロセス（C0用）の定義 ---
omp_proc = Process(pid=100)
omp_proc.cmd = [BINARY_PATH]
omp_proc.env = [
    f"GOMP_CPU_AFFINITY={affinity_order}",
    f"OMP_NUM_THREADS={num_threads}",
    "OMP_DYNAMIC=FALSE",
    "GOMP_SPINCOUNT=0"
]

# --- 3. CPUへのワークロード割り当て（真のマルチスレッド定石） ---
# 💡 コア0（マスター）だけに実体をセットします
all_cpus[0].workload = omp_proc
all_cpus[0].createThreads()

# 💡 コア1〜15には、別プロセスを立ち上げず、空のリストを明示的にセットして
# 「初期値は無いけれど、後からスレッドを受け入れる器」としてGem5のチェックを欺きます
dummy_pid = 200
for cpu in all_cpus[1:]:
    dummy = Process(pid=dummy_pid)
    dummy.cmd = [DUMMY]
    cpu.workload = dummy
    cpu.createThreads()
    dummy_pid+=1 
# --- 4. ワークロードの初期化とRoot生成 ---
system.workload = SEWorkload.init_compatible(BINARY_PATH)
root = Root(full_system=False, system=system)

# if STRATEGY == "Packed":
#     # Node0のBigコア優先で集中
#     active_indices = list(range(num_threads))  # [0,1,2,...,num_threads-1]

# elif STRATEGY == "Scatter":
#     # Node0とNode1を交互に使用
#     active_indices = []
#     for i in range(num_threads // 2):
#         active_indices.append(i)                    # Node0側
#         active_indices.append(i + (BIG_CORES_PER_NODE + SMALL_CORES_PER_NODE))  # Node1側
#     active_indices = active_indices[:num_threads]

# elif STRATEGY == "HPO":
#     # Bigコア(高クロック)を優先
#     big_node0  = list(range(0, BIG_CORES_PER_NODE))                    # [0,1,2,3]
#     big_node1  = list(range(8, 8 + BIG_CORES_PER_NODE))                # [8,9,10,11]
#     small_node0 = list(range(4, 4 + SMALL_CORES_PER_NODE))             # [4,5,6,7]
#     small_node1 = list(range(12, 12 + SMALL_CORES_PER_NODE))           # [12,13,14,15]
#     active_indices = (big_node0 + big_node1 + small_node0 + small_node1)[:num_threads]

# elif STRATEGY == "MPO":
#     # メモリ親和性優先：同一ノードペアでスレッドを束ねる
#     active_indices = [0,1,8,9, 2,3,10,11, 4,5,12,13, 6,7,14,15][:num_threads]

# else:
#     raise ValueError(f"Unknown STRATEGY: {STRATEGY}")

# print(f"active_indices: {active_indices}")

# # active_indicesのCPUにcpu_id=0,1,2,...を振り直す
# for new_id, cpu_idx in enumerate(active_indices):
#     all_cpus[cpu_idx].cpu_id = new_id
#     all_cpus[cpu_idx].workload = omp_proc
#     all_cpus[cpu_idx].createThreads()

# # 使わないCPUはdummy（cpu_idは既存のまま）
# used = set(active_indices)
# dummy_pid = 200
# for idx, cpu in enumerate(all_cpus):
#     if idx not in used:
#         dummy = Process(pid=dummy_pid)
#         dummy.cmd = [DUMMY]
#         cpu.workload = dummy
#         cpu.createThreads()
#         dummy_pid += 1

# system.workload = SEWorkload.init_compatible(BINARY_PATH)
# root = Root(full_system=False, system=system)


# debug printer

print(f"STRATEGY: {STRATEGY}")
print(f"num_threads: {NUM_THREADS}")
print(f"binary: {BINARY_PATH}")
import os
print(f"binary exists: {os.path.exists(BINARY_PATH)}")
print(f"DUMMY exists: {os.path.exists(DUMMY)}")
print(f"total CPUs: {len(all_cpus)}")
m5.instantiate()
NODE1_PHYS_BASE = MEM_STRIDE  # 0x40000000

try:
    omp_proc.map(
        vaddr=0x40000000,
        paddr=NODE1_PHYS_BASE,
        size=0x1000  # とりあえず1ページだけ
    )
    print("Process.map() 成功")
except Exception as e:
    print(f"Process.map() 失敗: {e}")
m5.simulate()
m5.stats.dump()
import re
stats_file = "m5out/stats.txt"
with open(stats_file) as f:
    content = f.read()

# 各ノードのメモリアクセス数を抽出
for node in ["node0", "node1"]:
    reads = re.search(rf"system\.{node}\.mem_ctrl\.readReqs\s+(\d+)", content)
    writes = re.search(rf"system\.{node}\.mem_ctrl\.writeReqs\s+(\d+)", content)
    print(f"{node}: reads={reads.group(1) if reads else 0}, writes={writes.group(1) if writes else 0}")
move_outputs_to_timestamped_dir(STRATEGY,NUM_NODES,BIG_CORES_PER_NODE,SMALL_CORES_PER_NODE)


