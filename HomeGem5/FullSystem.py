from gem5.components.boards.x86_board import X86Board
from gem5.components.memory.single_channel import SingleChannelDDR4_2400
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.components.processors.cpu_types import CPUTypes
from gem5.components.cachehierarchies.classic.private_l1_cache_hierarchy import PrivateL1CacheHierarchy
from gem5.resources.resource import obtain_resource
from gem5.simulate.simulator import Simulator
from gem5.isas import ISA
from datetime import datetime

# 1. キャッシュ階層とメモリのセットアップ
cache_hierarchy = PrivateL1CacheHierarchy(l1d_size="32KiB", l1i_size="32KiB")
memory = SingleChannelDDR4_2400(size="2GiB")

# 2. プロセッサのセットアップ（ここでKVMを指定！）
processor = SimpleProcessor(cpu_type=CPUTypes.KVM, num_cores=1,isa=ISA.X86)

# 3. ボードのセットアップ (X86DemoBoardの代わりにカスタム構成を適用)
board = X86Board(
    clk_freq="3GHz",
    processor=processor,
    memory=memory,
    cache_hierarchy=cache_hierarchy,
)

# 4. ワークロードの設定
board.set_workload(obtain_resource("x86-ubuntu-24.04-boot-no-systemd"))

# 5. シミュレータの実行
simulator = Simulator(board=board)

print("Start KVM boot:", datetime.now())
simulator.run()
print("End KVM boot:", datetime.now())