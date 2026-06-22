from typing import Any

class ABC:

    def __init__(self, *args, **kwargs) -> None: ...


class ABCMeta(type):

    def __init__(self, *args, **kwargs) -> None: ...


class AMPMPrefetcher(QueuedPrefetcher):
    ampm: Any
    latency: Any
    queue_size: Any
    max_prefetch_requests_with_pending_translation: Any
    queue_squash: Any
    queue_filter: Any
    cache_snoop: Any
    tag_prefetch: Any
    throttle_control_percentage: Any
    sys: Any
    block_size: Any
    on_miss: Any
    on_read: Any
    on_write: Any
    on_data: Any
    on_inst: Any
    prefetch_on_access: Any
    prefetch_on_pf_hit: Any
    use_virtual_addresses: Any
    page_bytes: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class AbstractMemory(ClockedObject):
    range: Any
    null: Any
    in_addr_map: Any
    kvm_map: Any
    conf_table_reported: Any
    image_file: Any
    writeable: Any
    collect_stats: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class AccessMapPatternMatching(ClockedObject):
    block_size: Any
    limit_stride: Any
    start_degree: Any
    hot_zone_size: Any
    access_map_table_entries: Any
    access_map_table_assoc: Any
    access_map_table_indexing_policy: Any
    access_map_table_replacement_policy: Any
    high_coverage_threshold: Any
    low_coverage_threshold: Any
    high_accuracy_threshold: Any
    low_accuracy_threshold: Any
    high_cache_hit_threshold: Any
    low_cache_hit_threshold: Any
    epoch_cycles: Any
    offchip_memory_latency: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Addr(CheckedInt):

    def __init__(self, *args, **kwargs) -> None: ...


class AddrMap(Enum):

    def __init__(self, *args, **kwargs) -> None: ...


class AddrMapper(SimObject):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class AddrRange(ParamValue):

    def __init__(self, *args, **kwargs) -> None: ...


class AtomicSimpleCPU(BaseAtomicSimpleCPU, X86CPU):
    width: Any
    simulate_data_stalls: Any
    simulate_inst_stalls: Any
    branchPred: Any
    system: Any
    cpu_id: Any
    socket_id: Any
    numThreads: Any
    pwr_gating_latency: Any
    power_gating_on_idle: Any
    function_trace: Any
    function_trace_start: Any
    checker: Any
    syscallRetryLatency: Any
    do_checkpoint_insts: Any
    do_statistics_insts: Any
    workload: Any
    mmu: Any
    interrupts: Any
    isa: Any
    decoder: Any
    max_insts_all_threads: Any
    max_insts_any_thread: Any
    simpoint_start_insts: Any
    progress_interval: Any
    switched_out: Any
    tracer: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BDI(MultiCompressor):
    compressors: Any
    encoding_in_tags: Any
    block_size: Any
    chunk_size_bits: Any
    size_threshold_percentage: Any
    comp_chunks_per_cycle: Any
    comp_extra_latency: Any
    decomp_chunks_per_cycle: Any
    decomp_extra_latency: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BIPRP(LRURP):
    btp: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BOPPrefetcher(QueuedPrefetcher):
    score_max: Any
    round_max: Any
    bad_score: Any
    rr_size: Any
    tag_bits: Any
    offset_list_size: Any
    negative_offsets_enable: Any
    delay_queue_enable: Any
    delay_queue_size: Any
    delay_queue_cycles: Any
    degree: Any
    latency: Any
    queue_size: Any
    max_prefetch_requests_with_pending_translation: Any
    queue_squash: Any
    queue_filter: Any
    cache_snoop: Any
    tag_prefetch: Any
    throttle_control_percentage: Any
    sys: Any
    block_size: Any
    on_miss: Any
    on_read: Any
    on_write: Any
    on_data: Any
    on_inst: Any
    prefetch_on_access: Any
    prefetch_on_pf_hit: Any
    use_virtual_addresses: Any
    page_bytes: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BRRIPRP(BaseReplacementPolicy):
    num_bits: Any
    hit_priority: Any
    btp: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BTBIndexingPolicy(SimObject):
    assoc: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BTBSetAssociative(BTBIndexingPolicy):
    num_entries: Any
    set_shift: Any
    tag_bits: Any
    numThreads: Any
    assoc: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BadAddr(IsaFake):
    ret_bad_addr: Any
    pio_size: Any
    ret_data8: Any
    ret_data16: Any
    ret_data32: Any
    ret_data64: Any
    update_data: Any
    warn_access: Any
    fake_mem: Any
    pio_addr: Any
    pio_latency: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BadDevice(BasicPioDevice):
    devicename: Any
    pio_addr: Any
    pio_latency: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Base16Delta8(BaseDictionaryCompressor):
    dictionary_size: Any
    block_size: Any
    chunk_size_bits: Any
    size_threshold_percentage: Any
    comp_chunks_per_cycle: Any
    comp_extra_latency: Any
    decomp_chunks_per_cycle: Any
    decomp_extra_latency: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Base32Delta16(BaseDictionaryCompressor):
    dictionary_size: Any
    block_size: Any
    chunk_size_bits: Any
    size_threshold_percentage: Any
    comp_chunks_per_cycle: Any
    comp_extra_latency: Any
    decomp_chunks_per_cycle: Any
    decomp_extra_latency: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Base32Delta8(BaseDictionaryCompressor):
    dictionary_size: Any
    block_size: Any
    chunk_size_bits: Any
    size_threshold_percentage: Any
    comp_chunks_per_cycle: Any
    comp_extra_latency: Any
    decomp_chunks_per_cycle: Any
    decomp_extra_latency: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Base64Delta16(BaseDictionaryCompressor):
    dictionary_size: Any
    block_size: Any
    chunk_size_bits: Any
    size_threshold_percentage: Any
    comp_chunks_per_cycle: Any
    comp_extra_latency: Any
    decomp_chunks_per_cycle: Any
    decomp_extra_latency: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Base64Delta32(BaseDictionaryCompressor):
    dictionary_size: Any
    block_size: Any
    chunk_size_bits: Any
    size_threshold_percentage: Any
    comp_chunks_per_cycle: Any
    comp_extra_latency: Any
    decomp_chunks_per_cycle: Any
    decomp_extra_latency: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Base64Delta8(BaseDictionaryCompressor):
    dictionary_size: Any
    block_size: Any
    chunk_size_bits: Any
    size_threshold_percentage: Any
    comp_chunks_per_cycle: Any
    comp_extra_latency: Any
    decomp_chunks_per_cycle: Any
    decomp_extra_latency: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BaseAtomicSimpleCPU(BaseSimpleCPU):
    width: Any
    simulate_data_stalls: Any
    simulate_inst_stalls: Any
    branchPred: Any
    system: Any
    cpu_id: Any
    socket_id: Any
    numThreads: Any
    pwr_gating_latency: Any
    power_gating_on_idle: Any
    function_trace: Any
    function_trace_start: Any
    checker: Any
    syscallRetryLatency: Any
    do_checkpoint_insts: Any
    do_statistics_insts: Any
    workload: Any
    mmu: Any
    interrupts: Any
    isa: Any
    decoder: Any
    max_insts_all_threads: Any
    max_insts_any_thread: Any
    simpoint_start_insts: Any
    progress_interval: Any
    switched_out: Any
    tracer: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BaseCPU(ClockedObject):
    system: Any
    cpu_id: Any
    socket_id: Any
    numThreads: Any
    pwr_gating_latency: Any
    power_gating_on_idle: Any
    function_trace: Any
    function_trace_start: Any
    checker: Any
    syscallRetryLatency: Any
    do_checkpoint_insts: Any
    do_statistics_insts: Any
    workload: Any
    mmu: Any
    interrupts: Any
    isa: Any
    decoder: Any
    max_insts_all_threads: Any
    max_insts_any_thread: Any
    simpoint_start_insts: Any
    progress_interval: Any
    switched_out: Any
    tracer: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BaseCache(ClockedObject):
    size: Any
    assoc: Any
    tag_latency: Any
    data_latency: Any
    response_latency: Any
    warmup_percentage: Any
    max_miss_count: Any
    mshrs: Any
    demand_mshr_reserve: Any
    tgts_per_mshr: Any
    write_buffers: Any
    is_read_only: Any
    prefetcher: Any
    tags: Any
    replacement_policy: Any
    partitioning_manager: Any
    compressor: Any
    replace_expansions: Any
    move_contractions: Any
    sequential_access: Any
    addr_ranges: Any
    system: Any
    writeback_clean: Any
    clusivity: Any
    write_allocator: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BaseCacheCompressor(SimObject):
    block_size: Any
    chunk_size_bits: Any
    size_threshold_percentage: Any
    comp_chunks_per_cycle: Any
    comp_extra_latency: Any
    decomp_chunks_per_cycle: Any
    decomp_extra_latency: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BaseDictionaryCompressor(BaseCacheCompressor):
    dictionary_size: Any
    block_size: Any
    chunk_size_bits: Any
    size_threshold_percentage: Any
    comp_chunks_per_cycle: Any
    comp_extra_latency: Any
    decomp_chunks_per_cycle: Any
    decomp_extra_latency: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BaseISA(SimObject):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BaseIndexingPolicy(SimObject):
    assoc: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BaseInterrupts(SimObject):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BaseKvmCPU(BaseCPU):
    usePerf: Any
    useCoalescedMMIO: Any
    usePerfOverflow: Any
    alwaysSyncTC: Any
    hostFreq: Any
    hostFactor: Any
    system: Any
    cpu_id: Any
    socket_id: Any
    numThreads: Any
    pwr_gating_latency: Any
    power_gating_on_idle: Any
    function_trace: Any
    function_trace_start: Any
    checker: Any
    syscallRetryLatency: Any
    do_checkpoint_insts: Any
    do_statistics_insts: Any
    workload: Any
    mmu: Any
    interrupts: Any
    isa: Any
    decoder: Any
    max_insts_all_threads: Any
    max_insts_any_thread: Any
    simpoint_start_insts: Any
    progress_interval: Any
    switched_out: Any
    tracer: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BaseMMU(SimObject):
    itb: Any
    dtb: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BaseMemProbe(SimObject):
    manager: Any
    probe_name: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BaseMinorCPU(BaseCPU):
    threadPolicy: Any
    fetch1FetchLimit: Any
    fetch1LineSnapWidth: Any
    fetch1LineWidth: Any
    fetch1ToFetch2ForwardDelay: Any
    fetch1ToFetch2BackwardDelay: Any
    fetch2InputBufferSize: Any
    fetch2ToDecodeForwardDelay: Any
    fetch2CycleInput: Any
    decodeInputBufferSize: Any
    decodeToExecuteForwardDelay: Any
    decodeInputWidth: Any
    decodeCycleInput: Any
    executeInputWidth: Any
    executeCycleInput: Any
    executeIssueLimit: Any
    executeMemoryIssueLimit: Any
    executeCommitLimit: Any
    executeMemoryCommitLimit: Any
    executeInputBufferSize: Any
    executeMemoryWidth: Any
    executeMaxAccessesInMemory: Any
    executeLSQMaxStoreBufferStoresPerCycle: Any
    executeLSQRequestsQueueSize: Any
    executeLSQTransfersQueueSize: Any
    executeLSQStoreBufferSize: Any
    executeBranchDelay: Any
    executeFuncUnits: Any
    executeSetTraceTimeOnCommit: Any
    executeSetTraceTimeOnIssue: Any
    executeAllowEarlyMemoryIssue: Any
    enableIdling: Any
    branchPred: Any
    system: Any
    cpu_id: Any
    socket_id: Any
    numThreads: Any
    pwr_gating_latency: Any
    power_gating_on_idle: Any
    function_trace: Any
    function_trace_start: Any
    checker: Any
    syscallRetryLatency: Any
    do_checkpoint_insts: Any
    do_statistics_insts: Any
    workload: Any
    mmu: Any
    interrupts: Any
    isa: Any
    decoder: Any
    max_insts_all_threads: Any
    max_insts_any_thread: Any
    simpoint_start_insts: Any
    progress_interval: Any
    switched_out: Any
    tracer: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BaseNonCachingSimpleCPU(BaseAtomicSimpleCPU):
    width: Any
    simulate_data_stalls: Any
    simulate_inst_stalls: Any
    branchPred: Any
    system: Any
    cpu_id: Any
    socket_id: Any
    numThreads: Any
    pwr_gating_latency: Any
    power_gating_on_idle: Any
    function_trace: Any
    function_trace_start: Any
    checker: Any
    syscallRetryLatency: Any
    do_checkpoint_insts: Any
    do_statistics_insts: Any
    workload: Any
    mmu: Any
    interrupts: Any
    isa: Any
    decoder: Any
    max_insts_all_threads: Any
    max_insts_any_thread: Any
    simpoint_start_insts: Any
    progress_interval: Any
    switched_out: Any
    tracer: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BaseO3CPU(BaseCPU):
    activity: Any
    cacheStorePorts: Any
    cacheLoadPorts: Any
    fetchToBacDelay: Any
    decodeToFetchDelay: Any
    renameToFetchDelay: Any
    iewToFetchDelay: Any
    commitToFetchDelay: Any
    fetchWidth: Any
    fetchBufferSize: Any
    fetchQueueSize: Any
    renameToDecodeDelay: Any
    iewToDecodeDelay: Any
    commitToDecodeDelay: Any
    bacToFetchDelay: Any
    fetchToDecodeDelay: Any
    decodeWidth: Any
    iewToRenameDelay: Any
    commitToRenameDelay: Any
    decodeToRenameDelay: Any
    renameWidth: Any
    commitToIEWDelay: Any
    renameToIEWDelay: Any
    issueToExecuteDelay: Any
    dispatchWidth: Any
    issueWidth: Any
    wbWidth: Any
    iewToCommitDelay: Any
    renameToROBDelay: Any
    commitWidth: Any
    squashWidth: Any
    trapLatency: Any
    fetchTrapLatency: Any
    backComSize: Any
    forwardComSize: Any
    LQEntries: Any
    SQEntries: Any
    LSQDepCheckShift: Any
    LSQCheckLoads: Any
    store_set_clear_period: Any
    LFSTSize: Any
    SSITSize: Any
    SSITAssoc: Any
    SSITReplPolicy: Any
    SSITIndexingPolicy: Any
    numRobs: Any
    numPhysIntRegs: Any
    numPhysFloatRegs: Any
    numPhysVecRegs: Any
    numPhysVecPredRegs: Any
    numPhysMatRegs: Any
    numPhysCCRegs: Any
    instQueues: Any
    numROBEntries: Any
    smtNumFetchingThreads: Any
    smtFetchPolicy: Any
    smtLSQPolicy: Any
    smtLSQThreshold: Any
    smtROBPolicy: Any
    smtROBThreshold: Any
    smtCommitPolicy: Any
    branchPred: Any
    needsTSO: Any
    recvRespThrottling: Any
    recvRespMaxCachelines: Any
    recvRespBufferSize: Any
    decoupledFrontEnd: Any
    numFTQEntries: Any
    minInstSize: Any
    fetchTargetWidth: Any
    maxFTPerCycle: Any
    maxTakenPredPerCycle: Any
    system: Any
    cpu_id: Any
    socket_id: Any
    numThreads: Any
    pwr_gating_latency: Any
    power_gating_on_idle: Any
    function_trace: Any
    function_trace_start: Any
    checker: Any
    syscallRetryLatency: Any
    do_checkpoint_insts: Any
    do_statistics_insts: Any
    workload: Any
    mmu: Any
    interrupts: Any
    isa: Any
    decoder: Any
    max_insts_all_threads: Any
    max_insts_any_thread: Any
    simpoint_start_insts: Any
    progress_interval: Any
    switched_out: Any
    tracer: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BaseO3Checker(CheckerCPU):
    exitOnError: Any
    updateOnError: Any
    warnOnlyOnLoadError: Any
    system: Any
    cpu_id: Any
    socket_id: Any
    numThreads: Any
    pwr_gating_latency: Any
    power_gating_on_idle: Any
    function_trace: Any
    function_trace_start: Any
    checker: Any
    syscallRetryLatency: Any
    do_checkpoint_insts: Any
    do_statistics_insts: Any
    workload: Any
    mmu: Any
    interrupts: Any
    isa: Any
    decoder: Any
    max_insts_all_threads: Any
    max_insts_any_thread: Any
    simpoint_start_insts: Any
    progress_interval: Any
    switched_out: Any
    tracer: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BasePartitioningPolicy(SimObject):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BasePrefetcher(ClockedObject):
    sys: Any
    block_size: Any
    on_miss: Any
    on_read: Any
    on_write: Any
    on_data: Any
    on_inst: Any
    prefetch_on_access: Any
    prefetch_on_pf_hit: Any
    use_virtual_addresses: Any
    page_bytes: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BaseReplacementPolicy(SimObject):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BaseRoutingUnit(SimObject):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BaseSetAssoc(BaseTags):
    assoc: Any
    replacement_policy: Any
    system: Any
    size: Any
    block_size: Any
    tag_latency: Any
    warmup_percentage: Any
    sequential_access: Any
    indexing_policy: Any
    partitioning_manager: Any
    entry_size: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BaseSimpleCPU(BaseCPU):
    branchPred: Any
    system: Any
    cpu_id: Any
    socket_id: Any
    numThreads: Any
    pwr_gating_latency: Any
    power_gating_on_idle: Any
    function_trace: Any
    function_trace_start: Any
    checker: Any
    syscallRetryLatency: Any
    do_checkpoint_insts: Any
    do_statistics_insts: Any
    workload: Any
    mmu: Any
    interrupts: Any
    isa: Any
    decoder: Any
    max_insts_all_threads: Any
    max_insts_any_thread: Any
    simpoint_start_insts: Any
    progress_interval: Any
    switched_out: Any
    tracer: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BaseTLB(SimObject):
    entry_type: Any
    next_level: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BaseTags(ClockedObject):
    system: Any
    size: Any
    block_size: Any
    tag_latency: Any
    warmup_percentage: Any
    sequential_access: Any
    indexing_policy: Any
    partitioning_manager: Any
    entry_size: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BaseTimingSimpleCPU(BaseSimpleCPU):
    branchPred: Any
    system: Any
    cpu_id: Any
    socket_id: Any
    numThreads: Any
    pwr_gating_latency: Any
    power_gating_on_idle: Any
    function_trace: Any
    function_trace_start: Any
    checker: Any
    syscallRetryLatency: Any
    do_checkpoint_insts: Any
    do_statistics_insts: Any
    workload: Any
    mmu: Any
    interrupts: Any
    isa: Any
    decoder: Any
    max_insts_all_threads: Any
    max_insts_any_thread: Any
    simpoint_start_insts: Any
    progress_interval: Any
    switched_out: Any
    tracer: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BaseTrafficGen(ClockedObject):
    system: Any
    elastic_req: Any
    max_outstanding_reqs: Any
    progress_check: Any
    stream_gen: Any
    sids: Any
    ssids: Any
    cpu_id: Any
    socket_id: Any
    numThreads: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BaseXBar(ClockedObject):
    frontend_latency: Any
    forward_latency: Any
    response_latency: Any
    header_latency: Any
    width: Any
    use_default_range: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BasicExtLink(BasicLink):
    ext_node: Any
    int_node: Any
    link_id: Any
    latency: Any
    bandwidth_factor: Any
    weight: Any
    supported_vnets: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BasicIntLink(BasicLink):
    src_node: Any
    dst_node: Any
    src_outport: Any
    dst_inport: Any
    link_id: Any
    latency: Any
    bandwidth_factor: Any
    weight: Any
    supported_vnets: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BasicLink(SimObject):
    link_id: Any
    latency: Any
    bandwidth_factor: Any
    weight: Any
    supported_vnets: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BasicPioDevice(PioDevice):
    pio_addr: Any
    pio_latency: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BasicRouter(ClockedObject):
    router_id: Any
    latency: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BiModeBP(ConditionalPredictor):
    globalPredictorSize: Any
    globalCtrBits: Any
    choicePredictorSize: Any
    choiceCtrBits: Any
    numThreads: Any
    instShiftAmt: Any
    speculativeHistUpdate: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BloomFilterBase(SimObject):
    size: Any
    offset_bits: Any
    num_bits: Any
    threshold: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BloomFilterBlock(BloomFilterBase):
    masks_lsbs: Any
    masks_sizes: Any
    size: Any
    offset_bits: Any
    num_bits: Any
    threshold: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BloomFilterBulk(BloomFilterMultiBitSel):
    num_hashes: Any
    skip_bits: Any
    is_parallel: Any
    size: Any
    offset_bits: Any
    num_bits: Any
    threshold: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BloomFilterH3(BloomFilterMultiBitSel):
    num_hashes: Any
    skip_bits: Any
    is_parallel: Any
    size: Any
    offset_bits: Any
    num_bits: Any
    threshold: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BloomFilterMulti(BloomFilterBase):
    filters: Any
    size: Any
    offset_bits: Any
    num_bits: Any
    threshold: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BloomFilterMultiBitSel(BloomFilterBase):
    num_hashes: Any
    skip_bits: Any
    is_parallel: Any
    size: Any
    offset_bits: Any
    num_bits: Any
    threshold: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BloomFilterPerfect(BloomFilterBase):
    size: Any
    offset_bits: Any
    num_bits: Any
    threshold: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Bool(ParamValue):

    def __init__(self, *args, **kwargs) -> None: ...


class BranchPredictor(SimObject):
    numThreads: Any
    instShiftAmt: Any
    speculativeHistUpdate: Any
    requiresBTBHit: Any
    updateBTBAtSquash: Any
    btb: Any
    ras: Any
    conditionalBranchPred: Any
    indirectBranchPred: Any
    takenOnlyHistory: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BranchTargetBuffer(ClockedObject):
    numThreads: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BranchType(Enum):

    def __init__(self, *args, **kwargs) -> None: ...


class Bridge(BridgeBase):
    ranges: Any
    req_size: Any
    resp_size: Any
    delay: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class BridgeBase(ClockedObject):
    req_size: Any
    resp_size: Any
    delay: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class ByteOrder(ScopedEnum):

    def __init__(self, *args, **kwargs) -> None: ...


class CDCType(Enum):

    def __init__(self, *args, **kwargs) -> None: ...


class CPack(BaseDictionaryCompressor):
    dictionary_size: Any
    block_size: Any
    chunk_size_bits: Any
    size_threshold_percentage: Any
    comp_chunks_per_cycle: Any
    comp_extra_latency: Any
    decomp_chunks_per_cycle: Any
    decomp_extra_latency: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Cache(BaseCache):
    size: Any
    assoc: Any
    tag_latency: Any
    data_latency: Any
    response_latency: Any
    warmup_percentage: Any
    max_miss_count: Any
    mshrs: Any
    demand_mshr_reserve: Any
    tgts_per_mshr: Any
    write_buffers: Any
    is_read_only: Any
    prefetcher: Any
    tags: Any
    replacement_policy: Any
    partitioning_manager: Any
    compressor: Any
    replace_expansions: Any
    move_contractions: Any
    sequential_access: Any
    addr_ranges: Any
    system: Any
    writeback_clean: Any
    clusivity: Any
    write_allocator: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class CfiMemory(AbstractMemory):
    latency: Any
    latency_var: Any
    bandwidth: Any
    vendor_id: Any
    device_id: Any
    blk_size: Any
    bank_width: Any
    range: Any
    null: Any
    in_addr_map: Any
    kvm_map: Any
    conf_table_reported: Any
    image_file: Any
    writeable: Any
    collect_stats: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Characteristic(Enum):

    def __init__(self, *args, **kwargs) -> None: ...


class CheckerCPU(BaseCPU):
    exitOnError: Any
    updateOnError: Any
    warnOnlyOnLoadError: Any
    system: Any
    cpu_id: Any
    socket_id: Any
    numThreads: Any
    pwr_gating_latency: Any
    power_gating_on_idle: Any
    function_trace: Any
    function_trace_start: Any
    checker: Any
    syscallRetryLatency: Any
    do_checkpoint_insts: Any
    do_statistics_insts: Any
    workload: Any
    mmu: Any
    interrupts: Any
    isa: Any
    decoder: Any
    max_insts_all_threads: Any
    max_insts_any_thread: Any
    simpoint_start_insts: Any
    progress_interval: Any
    switched_out: Any
    tracer: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Clock(TickParamValue):

    def __init__(self, *args, **kwargs) -> None: ...


class ClockDomain(SimObject):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class ClockedObject(SimObject):
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Clusivity(Enum):

    def __init__(self, *args, **kwargs) -> None: ...


class Cmos(BasicPioDevice):
    time: Any
    pio_addr: Any
    pio_latency: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class CoherentXBar(BaseXBar):
    snoop_response_latency: Any
    snoop_filter: Any
    max_outstanding_snoops: Any
    max_routing_table_size: Any
    point_of_coherency: Any
    point_of_unification: Any
    system: Any
    frontend_latency: Any
    forward_latency: Any
    response_latency: Any
    header_latency: Any
    width: Any
    use_default_range: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class CommMonitor(SimObject):
    system: Any
    sample_period: Any
    burst_length_bins: Any
    disable_burst_length_hists: Any
    bandwidth_bins: Any
    disable_bandwidth_hists: Any
    latency_bins: Any
    disable_latency_hists: Any
    itt_bins: Any
    itt_max_bin: Any
    disable_itt_dists: Any
    outstanding_bins: Any
    disable_outstanding_hists: Any
    transaction_bins: Any
    disable_transaction_hists: Any
    read_addr_mask: Any
    write_addr_mask: Any
    disable_addr_dists: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class CommitPolicy(ScopedEnum):

    def __init__(self, *args, **kwargs) -> None: ...


class CompressedTags(SectorTags):
    max_compression_ratio: Any
    assoc: Any
    num_blocks_per_sector: Any
    replacement_policy: Any
    system: Any
    size: Any
    block_size: Any
    tag_latency: Any
    warmup_percentage: Any
    sequential_access: Any
    indexing_policy: Any
    partitioning_manager: Any
    entry_size: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class ConditionalPredictor(SimObject):
    numThreads: Any
    instShiftAmt: Any
    speculativeHistUpdate: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class CopyEngine(PciEndpoint):
    ChanCnt: Any
    XferCap: Any
    latBeforeBegin: Any
    latAfterCompletion: Any
    BAR0: Any
    BAR1: Any
    BAR2: Any
    BAR3: Any
    BAR4: Any
    BAR5: Any
    CardbusCIS: Any
    SubsystemID: Any
    SubsystemVendorID: Any
    ExpansionROM: Any
    MaximumLatency: Any
    MinimumGrant: Any
    upstream: Any
    pci_dev: Any
    pci_func: Any
    pio_latency: Any
    config_latency: Any
    VendorID: Any
    DeviceID: Any
    Command: Any
    Status: Any
    Revision: Any
    ProgIF: Any
    SubClassCode: Any
    ClassCode: Any
    CacheLineSize: Any
    LatencyTimer: Any
    HeaderType: Any
    BIST: Any
    CapabilityPtr: Any
    InterruptLine: Any
    InterruptPin: Any
    PMCAPBaseOffset: Any
    PMCAPNextCapability: Any
    PMCAPCapId: Any
    PMCAPCapabilities: Any
    PMCAPCtrlStatus: Any
    MSICAPBaseOffset: Any
    MSICAPNextCapability: Any
    MSICAPCapId: Any
    MSICAPMsgCtrl: Any
    MSICAPMsgAddr: Any
    MSICAPMsgUpperAddr: Any
    MSICAPMsgData: Any
    MSICAPMaskBits: Any
    MSICAPPendingBits: Any
    MSIXCAPBaseOffset: Any
    MSIXCAPNextCapability: Any
    MSIXCAPCapId: Any
    MSIXMsgCtrl: Any
    MSIXTableOffset: Any
    MSIXPbaOffset: Any
    PXCAPBaseOffset: Any
    PXCAPNextCapability: Any
    PXCAPCapId: Any
    PXCAPCapabilities: Any
    PXCAPDevCapabilities: Any
    PXCAPDevCtrl: Any
    PXCAPDevStatus: Any
    PXCAPLinkCap: Any
    PXCAPLinkCtrl: Any
    PXCAPLinkStatus: Any
    PXCAPSlotCap: Any
    PXCAPSlotCtrl: Any
    PXCAPSlotStatus: Any
    PXCAPRootCap: Any
    PXCAPRootCtrl: Any
    PXCAPRootStatus: Any
    PXCAPDevCap2: Any
    PXCAPDevCtrl2: Any
    PXCAPDevStatus2: Any
    PXCAPLinkCap2: Any
    PXCAPLinkCtrl2: Any
    PXCAPLinkStatus2: Any
    PXCAPSlotCap2: Any
    PXCAPSlotCtrl2: Any
    PXCAPSlotStatus2: Any
    sid: Any
    ssid: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Counter(CheckedInt):

    def __init__(self, *args, **kwargs) -> None: ...


class CowDiskImage(DiskImage):
    child: Any
    table_size: Any
    image_file: Any
    read_only: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class CpuCluster(SubSystem):
    voltage_domain: Any
    clk_domain: Any
    thermal_domain: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class CreditLink(NetworkLink):
    link_id: Any
    link_latency: Any
    vcs_per_vnet: Any
    virt_nets: Any
    supported_vnets: Any
    width: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Current(Float):

    def __init__(self, *args, **kwargs) -> None: ...


class Cycles(CheckedInt):

    def __init__(self, *args, **kwargs) -> None: ...


class DCPTPrefetcher(QueuedPrefetcher):
    dcpt: Any
    latency: Any
    queue_size: Any
    max_prefetch_requests_with_pending_translation: Any
    queue_squash: Any
    queue_filter: Any
    cache_snoop: Any
    tag_prefetch: Any
    throttle_control_percentage: Any
    sys: Any
    block_size: Any
    on_miss: Any
    on_read: Any
    on_write: Any
    on_data: Any
    on_inst: Any
    prefetch_on_access: Any
    prefetch_on_pf_hit: Any
    use_virtual_addresses: Any
    page_bytes: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class DDR3_1600_8x8(DRAMInterface):
    page_policy: Any
    max_accesses_per_row: Any
    bank_groups_per_rank: Any
    enable_dram_powerdown: Any
    dll: Any
    tRCD: Any
    tRCD_WR: Any
    tCL: Any
    tCWL: Any
    tRP: Any
    tRAS: Any
    tWR: Any
    tRTP: Any
    tBURST_MAX: Any
    tBURST_MIN: Any
    tCCD_L: Any
    tCCD_L_WR: Any
    tRFC: Any
    tREFI: Any
    tWTR_L: Any
    tPPD: Any
    tAAD: Any
    two_cycle_activate: Any
    tRRD: Any
    tRRD_L: Any
    tXAW: Any
    activation_limit: Any
    tXP: Any
    tXPDLL: Any
    tXS: Any
    tXSDLL: Any
    beats_per_clock: Any
    data_clock_sync: Any
    IDD0: Any
    IDD02: Any
    IDD2P0: Any
    IDD2P02: Any
    IDD2P1: Any
    IDD2P12: Any
    IDD2N: Any
    IDD2N2: Any
    IDD3P0: Any
    IDD3P02: Any
    IDD3P1: Any
    IDD3P12: Any
    IDD3N: Any
    IDD3N2: Any
    IDD4R: Any
    IDD4R2: Any
    IDD4W: Any
    IDD4W2: Any
    IDD5: Any
    IDD52: Any
    IDD6: Any
    IDD62: Any
    VDD: Any
    VDD2: Any
    write_buffer_size: Any
    read_buffer_size: Any
    addr_mapping: Any
    device_size: Any
    device_bus_width: Any
    burst_length: Any
    device_rowbuffer_size: Any
    devices_per_rank: Any
    ranks_per_channel: Any
    banks_per_rank: Any
    tCK: Any
    tBURST: Any
    tWTR: Any
    tRTW: Any
    tCS: Any
    range: Any
    null: Any
    in_addr_map: Any
    kvm_map: Any
    conf_table_reported: Any
    image_file: Any
    writeable: Any
    collect_stats: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class DDR3_2133_8x8(DDR3_1600_8x8):
    page_policy: Any
    max_accesses_per_row: Any
    bank_groups_per_rank: Any
    enable_dram_powerdown: Any
    dll: Any
    tRCD: Any
    tRCD_WR: Any
    tCL: Any
    tCWL: Any
    tRP: Any
    tRAS: Any
    tWR: Any
    tRTP: Any
    tBURST_MAX: Any
    tBURST_MIN: Any
    tCCD_L: Any
    tCCD_L_WR: Any
    tRFC: Any
    tREFI: Any
    tWTR_L: Any
    tPPD: Any
    tAAD: Any
    two_cycle_activate: Any
    tRRD: Any
    tRRD_L: Any
    tXAW: Any
    activation_limit: Any
    tXP: Any
    tXPDLL: Any
    tXS: Any
    tXSDLL: Any
    beats_per_clock: Any
    data_clock_sync: Any
    IDD0: Any
    IDD02: Any
    IDD2P0: Any
    IDD2P02: Any
    IDD2P1: Any
    IDD2P12: Any
    IDD2N: Any
    IDD2N2: Any
    IDD3P0: Any
    IDD3P02: Any
    IDD3P1: Any
    IDD3P12: Any
    IDD3N: Any
    IDD3N2: Any
    IDD4R: Any
    IDD4R2: Any
    IDD4W: Any
    IDD4W2: Any
    IDD5: Any
    IDD52: Any
    IDD6: Any
    IDD62: Any
    VDD: Any
    VDD2: Any
    write_buffer_size: Any
    read_buffer_size: Any
    addr_mapping: Any
    device_size: Any
    device_bus_width: Any
    burst_length: Any
    device_rowbuffer_size: Any
    devices_per_rank: Any
    ranks_per_channel: Any
    banks_per_rank: Any
    tCK: Any
    tBURST: Any
    tWTR: Any
    tRTW: Any
    tCS: Any
    range: Any
    null: Any
    in_addr_map: Any
    kvm_map: Any
    conf_table_reported: Any
    image_file: Any
    writeable: Any
    collect_stats: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class DDR4_2400_16x4(DRAMInterface):
    page_policy: Any
    max_accesses_per_row: Any
    bank_groups_per_rank: Any
    enable_dram_powerdown: Any
    dll: Any
    tRCD: Any
    tRCD_WR: Any
    tCL: Any
    tCWL: Any
    tRP: Any
    tRAS: Any
    tWR: Any
    tRTP: Any
    tBURST_MAX: Any
    tBURST_MIN: Any
    tCCD_L: Any
    tCCD_L_WR: Any
    tRFC: Any
    tREFI: Any
    tWTR_L: Any
    tPPD: Any
    tAAD: Any
    two_cycle_activate: Any
    tRRD: Any
    tRRD_L: Any
    tXAW: Any
    activation_limit: Any
    tXP: Any
    tXPDLL: Any
    tXS: Any
    tXSDLL: Any
    beats_per_clock: Any
    data_clock_sync: Any
    IDD0: Any
    IDD02: Any
    IDD2P0: Any
    IDD2P02: Any
    IDD2P1: Any
    IDD2P12: Any
    IDD2N: Any
    IDD2N2: Any
    IDD3P0: Any
    IDD3P02: Any
    IDD3P1: Any
    IDD3P12: Any
    IDD3N: Any
    IDD3N2: Any
    IDD4R: Any
    IDD4R2: Any
    IDD4W: Any
    IDD4W2: Any
    IDD5: Any
    IDD52: Any
    IDD6: Any
    IDD62: Any
    VDD: Any
    VDD2: Any
    write_buffer_size: Any
    read_buffer_size: Any
    addr_mapping: Any
    device_size: Any
    device_bus_width: Any
    burst_length: Any
    device_rowbuffer_size: Any
    devices_per_rank: Any
    ranks_per_channel: Any
    banks_per_rank: Any
    tCK: Any
    tBURST: Any
    tWTR: Any
    tRTW: Any
    tCS: Any
    range: Any
    null: Any
    in_addr_map: Any
    kvm_map: Any
    conf_table_reported: Any
    image_file: Any
    writeable: Any
    collect_stats: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class DDR4_2400_4x16(DDR4_2400_16x4):
    page_policy: Any
    max_accesses_per_row: Any
    bank_groups_per_rank: Any
    enable_dram_powerdown: Any
    dll: Any
    tRCD: Any
    tRCD_WR: Any
    tCL: Any
    tCWL: Any
    tRP: Any
    tRAS: Any
    tWR: Any
    tRTP: Any
    tBURST_MAX: Any
    tBURST_MIN: Any
    tCCD_L: Any
    tCCD_L_WR: Any
    tRFC: Any
    tREFI: Any
    tWTR_L: Any
    tPPD: Any
    tAAD: Any
    two_cycle_activate: Any
    tRRD: Any
    tRRD_L: Any
    tXAW: Any
    activation_limit: Any
    tXP: Any
    tXPDLL: Any
    tXS: Any
    tXSDLL: Any
    beats_per_clock: Any
    data_clock_sync: Any
    IDD0: Any
    IDD02: Any
    IDD2P0: Any
    IDD2P02: Any
    IDD2P1: Any
    IDD2P12: Any
    IDD2N: Any
    IDD2N2: Any
    IDD3P0: Any
    IDD3P02: Any
    IDD3P1: Any
    IDD3P12: Any
    IDD3N: Any
    IDD3N2: Any
    IDD4R: Any
    IDD4R2: Any
    IDD4W: Any
    IDD4W2: Any
    IDD5: Any
    IDD52: Any
    IDD6: Any
    IDD62: Any
    VDD: Any
    VDD2: Any
    write_buffer_size: Any
    read_buffer_size: Any
    addr_mapping: Any
    device_size: Any
    device_bus_width: Any
    burst_length: Any
    device_rowbuffer_size: Any
    devices_per_rank: Any
    ranks_per_channel: Any
    banks_per_rank: Any
    tCK: Any
    tBURST: Any
    tWTR: Any
    tRTW: Any
    tCS: Any
    range: Any
    null: Any
    in_addr_map: Any
    kvm_map: Any
    conf_table_reported: Any
    image_file: Any
    writeable: Any
    collect_stats: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class DDR4_2400_8x8(DDR4_2400_16x4):
    page_policy: Any
    max_accesses_per_row: Any
    bank_groups_per_rank: Any
    enable_dram_powerdown: Any
    dll: Any
    tRCD: Any
    tRCD_WR: Any
    tCL: Any
    tCWL: Any
    tRP: Any
    tRAS: Any
    tWR: Any
    tRTP: Any
    tBURST_MAX: Any
    tBURST_MIN: Any
    tCCD_L: Any
    tCCD_L_WR: Any
    tRFC: Any
    tREFI: Any
    tWTR_L: Any
    tPPD: Any
    tAAD: Any
    two_cycle_activate: Any
    tRRD: Any
    tRRD_L: Any
    tXAW: Any
    activation_limit: Any
    tXP: Any
    tXPDLL: Any
    tXS: Any
    tXSDLL: Any
    beats_per_clock: Any
    data_clock_sync: Any
    IDD0: Any
    IDD02: Any
    IDD2P0: Any
    IDD2P02: Any
    IDD2P1: Any
    IDD2P12: Any
    IDD2N: Any
    IDD2N2: Any
    IDD3P0: Any
    IDD3P02: Any
    IDD3P1: Any
    IDD3P12: Any
    IDD3N: Any
    IDD3N2: Any
    IDD4R: Any
    IDD4R2: Any
    IDD4W: Any
    IDD4W2: Any
    IDD5: Any
    IDD52: Any
    IDD6: Any
    IDD62: Any
    VDD: Any
    VDD2: Any
    write_buffer_size: Any
    read_buffer_size: Any
    addr_mapping: Any
    device_size: Any
    device_bus_width: Any
    burst_length: Any
    device_rowbuffer_size: Any
    devices_per_rank: Any
    ranks_per_channel: Any
    banks_per_rank: Any
    tCK: Any
    tBURST: Any
    tWTR: Any
    tRTW: Any
    tCS: Any
    range: Any
    null: Any
    in_addr_map: Any
    kvm_map: Any
    conf_table_reported: Any
    image_file: Any
    writeable: Any
    collect_stats: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class DDR5_4400_4x8(DRAMInterface):
    page_policy: Any
    max_accesses_per_row: Any
    bank_groups_per_rank: Any
    enable_dram_powerdown: Any
    dll: Any
    tRCD: Any
    tRCD_WR: Any
    tCL: Any
    tCWL: Any
    tRP: Any
    tRAS: Any
    tWR: Any
    tRTP: Any
    tBURST_MAX: Any
    tBURST_MIN: Any
    tCCD_L: Any
    tCCD_L_WR: Any
    tRFC: Any
    tREFI: Any
    tWTR_L: Any
    tPPD: Any
    tAAD: Any
    two_cycle_activate: Any
    tRRD: Any
    tRRD_L: Any
    tXAW: Any
    activation_limit: Any
    tXP: Any
    tXPDLL: Any
    tXS: Any
    tXSDLL: Any
    beats_per_clock: Any
    data_clock_sync: Any
    IDD0: Any
    IDD02: Any
    IDD2P0: Any
    IDD2P02: Any
    IDD2P1: Any
    IDD2P12: Any
    IDD2N: Any
    IDD2N2: Any
    IDD3P0: Any
    IDD3P02: Any
    IDD3P1: Any
    IDD3P12: Any
    IDD3N: Any
    IDD3N2: Any
    IDD4R: Any
    IDD4R2: Any
    IDD4W: Any
    IDD4W2: Any
    IDD5: Any
    IDD52: Any
    IDD6: Any
    IDD62: Any
    VDD: Any
    VDD2: Any
    write_buffer_size: Any
    read_buffer_size: Any
    addr_mapping: Any
    device_size: Any
    device_bus_width: Any
    burst_length: Any
    device_rowbuffer_size: Any
    devices_per_rank: Any
    ranks_per_channel: Any
    banks_per_rank: Any
    tCK: Any
    tBURST: Any
    tWTR: Any
    tRTW: Any
    tCS: Any
    range: Any
    null: Any
    in_addr_map: Any
    kvm_map: Any
    conf_table_reported: Any
    image_file: Any
    writeable: Any
    collect_stats: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class DDR5_6400_4x8(DDR5_4400_4x8):
    page_policy: Any
    max_accesses_per_row: Any
    bank_groups_per_rank: Any
    enable_dram_powerdown: Any
    dll: Any
    tRCD: Any
    tRCD_WR: Any
    tCL: Any
    tCWL: Any
    tRP: Any
    tRAS: Any
    tWR: Any
    tRTP: Any
    tBURST_MAX: Any
    tBURST_MIN: Any
    tCCD_L: Any
    tCCD_L_WR: Any
    tRFC: Any
    tREFI: Any
    tWTR_L: Any
    tPPD: Any
    tAAD: Any
    two_cycle_activate: Any
    tRRD: Any
    tRRD_L: Any
    tXAW: Any
    activation_limit: Any
    tXP: Any
    tXPDLL: Any
    tXS: Any
    tXSDLL: Any
    beats_per_clock: Any
    data_clock_sync: Any
    IDD0: Any
    IDD02: Any
    IDD2P0: Any
    IDD2P02: Any
    IDD2P1: Any
    IDD2P12: Any
    IDD2N: Any
    IDD2N2: Any
    IDD3P0: Any
    IDD3P02: Any
    IDD3P1: Any
    IDD3P12: Any
    IDD3N: Any
    IDD3N2: Any
    IDD4R: Any
    IDD4R2: Any
    IDD4W: Any
    IDD4W2: Any
    IDD5: Any
    IDD52: Any
    IDD6: Any
    IDD62: Any
    VDD: Any
    VDD2: Any
    write_buffer_size: Any
    read_buffer_size: Any
    addr_mapping: Any
    device_size: Any
    device_bus_width: Any
    burst_length: Any
    device_rowbuffer_size: Any
    devices_per_rank: Any
    ranks_per_channel: Any
    banks_per_rank: Any
    tCK: Any
    tBURST: Any
    tWTR: Any
    tRTW: Any
    tCS: Any
    range: Any
    null: Any
    in_addr_map: Any
    kvm_map: Any
    conf_table_reported: Any
    image_file: Any
    writeable: Any
    collect_stats: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class DDR5_8400_4x8(DDR5_4400_4x8):
    page_policy: Any
    max_accesses_per_row: Any
    bank_groups_per_rank: Any
    enable_dram_powerdown: Any
    dll: Any
    tRCD: Any
    tRCD_WR: Any
    tCL: Any
    tCWL: Any
    tRP: Any
    tRAS: Any
    tWR: Any
    tRTP: Any
    tBURST_MAX: Any
    tBURST_MIN: Any
    tCCD_L: Any
    tCCD_L_WR: Any
    tRFC: Any
    tREFI: Any
    tWTR_L: Any
    tPPD: Any
    tAAD: Any
    two_cycle_activate: Any
    tRRD: Any
    tRRD_L: Any
    tXAW: Any
    activation_limit: Any
    tXP: Any
    tXPDLL: Any
    tXS: Any
    tXSDLL: Any
    beats_per_clock: Any
    data_clock_sync: Any
    IDD0: Any
    IDD02: Any
    IDD2P0: Any
    IDD2P02: Any
    IDD2P1: Any
    IDD2P12: Any
    IDD2N: Any
    IDD2N2: Any
    IDD3P0: Any
    IDD3P02: Any
    IDD3P1: Any
    IDD3P12: Any
    IDD3N: Any
    IDD3N2: Any
    IDD4R: Any
    IDD4R2: Any
    IDD4W: Any
    IDD4W2: Any
    IDD5: Any
    IDD52: Any
    IDD6: Any
    IDD62: Any
    VDD: Any
    VDD2: Any
    write_buffer_size: Any
    read_buffer_size: Any
    addr_mapping: Any
    device_size: Any
    device_bus_width: Any
    burst_length: Any
    device_rowbuffer_size: Any
    devices_per_rank: Any
    ranks_per_channel: Any
    banks_per_rank: Any
    tCK: Any
    tBURST: Any
    tWTR: Any
    tRTW: Any
    tCS: Any
    range: Any
    null: Any
    in_addr_map: Any
    kvm_map: Any
    conf_table_reported: Any
    image_file: Any
    writeable: Any
    collect_stats: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class DMASequencer(RubyPort):
    max_outstanding_requests: Any
    version: Any
    using_ruby_tester: Any
    no_retry_on_stall: Any
    ruby_system: Any
    system: Any
    support_data_reqs: Any
    support_inst_reqs: Any
    is_cpu_sequencer: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class DMA_Controller(MESI_Two_Level_DMA_Controller):
    dma_sequencer: Any
    request_latency: Any
    responseFromDir: Any
    requestToDir: Any
    mandatoryQueue: Any
    version: Any
    addr_ranges: Any
    cluster_id: Any
    transitions_per_cycle: Any
    buffer_size: Any
    recycle_latency: Any
    number_of_TBEs: Any
    ruby_system: Any
    mandatory_queue_latency: Any
    system: Any
    upstream_destinations: Any
    downstream_destinations: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class DRAMInterface(MemInterface):
    page_policy: Any
    max_accesses_per_row: Any
    bank_groups_per_rank: Any
    enable_dram_powerdown: Any
    dll: Any
    tRCD: Any
    tRCD_WR: Any
    tCL: Any
    tCWL: Any
    tRP: Any
    tRAS: Any
    tWR: Any
    tRTP: Any
    tBURST_MAX: Any
    tBURST_MIN: Any
    tCCD_L: Any
    tCCD_L_WR: Any
    tRFC: Any
    tREFI: Any
    tWTR_L: Any
    tPPD: Any
    tAAD: Any
    two_cycle_activate: Any
    tRRD: Any
    tRRD_L: Any
    tXAW: Any
    activation_limit: Any
    tXP: Any
    tXPDLL: Any
    tXS: Any
    tXSDLL: Any
    beats_per_clock: Any
    data_clock_sync: Any
    IDD0: Any
    IDD02: Any
    IDD2P0: Any
    IDD2P02: Any
    IDD2P1: Any
    IDD2P12: Any
    IDD2N: Any
    IDD2N2: Any
    IDD3P0: Any
    IDD3P02: Any
    IDD3P1: Any
    IDD3P12: Any
    IDD3N: Any
    IDD3N2: Any
    IDD4R: Any
    IDD4R2: Any
    IDD4W: Any
    IDD4W2: Any
    IDD5: Any
    IDD52: Any
    IDD6: Any
    IDD62: Any
    VDD: Any
    VDD2: Any
    write_buffer_size: Any
    read_buffer_size: Any
    addr_mapping: Any
    device_size: Any
    device_bus_width: Any
    burst_length: Any
    device_rowbuffer_size: Any
    devices_per_rank: Any
    ranks_per_channel: Any
    banks_per_rank: Any
    tCK: Any
    tBURST: Any
    tWTR: Any
    tRTW: Any
    tCS: Any
    range: Any
    null: Any
    in_addr_map: Any
    kvm_map: Any
    conf_table_reported: Any
    image_file: Any
    writeable: Any
    collect_stats: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class DRRIPRP(DuelingRP):
    constituency_size: Any
    team_size: Any
    replacement_policy_a: Any
    replacement_policy_b: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class DVFSHandler(SimObject):
    domains: Any
    sys_clk_domain: Any
    enable: Any
    transition_latency: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class DefaultFUPool(FUPool):
    FUList: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class DefaultX86FUPool(FUPool):
    FUList: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class DeltaCorrelatingPredictionTables(SimObject):
    deltas_per_entry: Any
    delta_bits: Any
    delta_mask_bits: Any
    table_entries: Any
    table_assoc: Any
    table_indexing_policy: Any
    table_replacement_policy: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class DeprecatedParam:

    def __init__(self, *args, **kwargs) -> None: ...


class DerivO3CPU(BaseO3CPU, X86CPU):
    activity: Any
    cacheStorePorts: Any
    cacheLoadPorts: Any
    fetchToBacDelay: Any
    decodeToFetchDelay: Any
    renameToFetchDelay: Any
    iewToFetchDelay: Any
    commitToFetchDelay: Any
    fetchWidth: Any
    fetchBufferSize: Any
    fetchQueueSize: Any
    renameToDecodeDelay: Any
    iewToDecodeDelay: Any
    commitToDecodeDelay: Any
    bacToFetchDelay: Any
    fetchToDecodeDelay: Any
    decodeWidth: Any
    iewToRenameDelay: Any
    commitToRenameDelay: Any
    decodeToRenameDelay: Any
    renameWidth: Any
    commitToIEWDelay: Any
    renameToIEWDelay: Any
    issueToExecuteDelay: Any
    dispatchWidth: Any
    issueWidth: Any
    wbWidth: Any
    iewToCommitDelay: Any
    renameToROBDelay: Any
    commitWidth: Any
    squashWidth: Any
    trapLatency: Any
    fetchTrapLatency: Any
    backComSize: Any
    forwardComSize: Any
    LQEntries: Any
    SQEntries: Any
    LSQDepCheckShift: Any
    LSQCheckLoads: Any
    store_set_clear_period: Any
    LFSTSize: Any
    SSITSize: Any
    SSITAssoc: Any
    SSITReplPolicy: Any
    SSITIndexingPolicy: Any
    numRobs: Any
    numPhysIntRegs: Any
    numPhysFloatRegs: Any
    numPhysVecRegs: Any
    numPhysVecPredRegs: Any
    numPhysMatRegs: Any
    numPhysCCRegs: Any
    instQueues: Any
    numROBEntries: Any
    smtNumFetchingThreads: Any
    smtFetchPolicy: Any
    smtLSQPolicy: Any
    smtLSQThreshold: Any
    smtROBPolicy: Any
    smtROBThreshold: Any
    smtCommitPolicy: Any
    branchPred: Any
    needsTSO: Any
    recvRespThrottling: Any
    recvRespMaxCachelines: Any
    recvRespBufferSize: Any
    decoupledFrontEnd: Any
    numFTQEntries: Any
    minInstSize: Any
    fetchTargetWidth: Any
    maxFTPerCycle: Any
    maxTakenPredPerCycle: Any
    system: Any
    cpu_id: Any
    socket_id: Any
    numThreads: Any
    pwr_gating_latency: Any
    power_gating_on_idle: Any
    function_trace: Any
    function_trace_start: Any
    checker: Any
    syscallRetryLatency: Any
    do_checkpoint_insts: Any
    do_statistics_insts: Any
    workload: Any
    mmu: Any
    interrupts: Any
    isa: Any
    decoder: Any
    max_insts_all_threads: Any
    max_insts_any_thread: Any
    simpoint_start_insts: Any
    progress_interval: Any
    switched_out: Any
    tracer: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class DerivedClockDomain(ClockDomain):
    clk_domain: Any
    clk_divider: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class DictParamDesc(ParamDesc):

    def __init__(self, *args, **kwargs) -> None: ...


class DictParamValue(dict):

    def __init__(self, *args, **kwargs) -> None: ...


class DirectedGenerator(SimObject):
    num_cpus: Any
    system: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Directory_Controller(MESI_Two_Level_Directory_Controller):
    directory: Any
    to_mem_ctrl_latency: Any
    directory_latency: Any
    requestToDir: Any
    responseToDir: Any
    responseFromDir: Any
    requestToMemory: Any
    responseFromMemory: Any
    version: Any
    addr_ranges: Any
    cluster_id: Any
    transitions_per_cycle: Any
    buffer_size: Any
    recycle_latency: Any
    number_of_TBEs: Any
    ruby_system: Any
    mandatory_queue_latency: Any
    system: Any
    upstream_destinations: Any
    downstream_destinations: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class DiskImage(SimObject):
    image_file: Any
    read_only: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class DistEtherLink(SimObject):
    delay: Any
    delay_var: Any
    speed: Any
    dump: Any
    dist_rank: Any
    dist_size: Any
    sync_start: Any
    sync_repeat: Any
    server_name: Any
    server_port: Any
    is_switch: Any
    dist_sync_on_pseudo_op: Any
    num_nodes: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class DmaDevice(PioDevice):
    sid: Any
    ssid: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class DmaVirtDevice(DmaDevice):
    sid: Any
    ssid: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class DuelingRP(BaseReplacementPolicy):
    constituency_size: Any
    team_size: Any
    replacement_policy_a: Any
    replacement_policy_b: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class DummyChecker(CheckerCPU):
    exitOnError: Any
    updateOnError: Any
    warnOnlyOnLoadError: Any
    system: Any
    cpu_id: Any
    socket_id: Any
    numThreads: Any
    pwr_gating_latency: Any
    power_gating_on_idle: Any
    function_trace: Any
    function_trace_start: Any
    checker: Any
    syscallRetryLatency: Any
    do_checkpoint_insts: Any
    do_statistics_insts: Any
    workload: Any
    mmu: Any
    interrupts: Any
    isa: Any
    decoder: Any
    max_insts_all_threads: Any
    max_insts_any_thread: Any
    simpoint_start_insts: Any
    progress_interval: Any
    switched_out: Any
    tracer: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class ElasticTrace(ProbeListenerObject):
    instFetchTraceFile: Any
    dataDepTraceFile: Any
    depWindowSize: Any
    startTraceInst: Any
    traceVirtAddr: Any
    manager: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class EmulatedDriver(SimObject):
    filename: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Energy(Float):

    def __init__(self, *args, **kwargs) -> None: ...


class Enum(ParamValue):

    def __init__(self, *args, **kwargs) -> None: ...


class EtherBus(SimObject):
    loopback: Any
    dump: Any
    speed: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class EtherDevBase(EtherDevice):
    hardware_address: Any
    dma_read_delay: Any
    dma_read_factor: Any
    dma_write_delay: Any
    dma_write_factor: Any
    rx_delay: Any
    tx_delay: Any
    rx_fifo_size: Any
    tx_fifo_size: Any
    rx_filter: Any
    intr_delay: Any
    rx_thread: Any
    tx_thread: Any
    rss: Any
    BAR0: Any
    BAR1: Any
    BAR2: Any
    BAR3: Any
    BAR4: Any
    BAR5: Any
    CardbusCIS: Any
    SubsystemID: Any
    SubsystemVendorID: Any
    ExpansionROM: Any
    MaximumLatency: Any
    MinimumGrant: Any
    upstream: Any
    pci_dev: Any
    pci_func: Any
    pio_latency: Any
    config_latency: Any
    VendorID: Any
    DeviceID: Any
    Command: Any
    Status: Any
    Revision: Any
    ProgIF: Any
    SubClassCode: Any
    ClassCode: Any
    CacheLineSize: Any
    LatencyTimer: Any
    HeaderType: Any
    BIST: Any
    CapabilityPtr: Any
    InterruptLine: Any
    InterruptPin: Any
    PMCAPBaseOffset: Any
    PMCAPNextCapability: Any
    PMCAPCapId: Any
    PMCAPCapabilities: Any
    PMCAPCtrlStatus: Any
    MSICAPBaseOffset: Any
    MSICAPNextCapability: Any
    MSICAPCapId: Any
    MSICAPMsgCtrl: Any
    MSICAPMsgAddr: Any
    MSICAPMsgUpperAddr: Any
    MSICAPMsgData: Any
    MSICAPMaskBits: Any
    MSICAPPendingBits: Any
    MSIXCAPBaseOffset: Any
    MSIXCAPNextCapability: Any
    MSIXCAPCapId: Any
    MSIXMsgCtrl: Any
    MSIXTableOffset: Any
    MSIXPbaOffset: Any
    PXCAPBaseOffset: Any
    PXCAPNextCapability: Any
    PXCAPCapId: Any
    PXCAPCapabilities: Any
    PXCAPDevCapabilities: Any
    PXCAPDevCtrl: Any
    PXCAPDevStatus: Any
    PXCAPLinkCap: Any
    PXCAPLinkCtrl: Any
    PXCAPLinkStatus: Any
    PXCAPSlotCap: Any
    PXCAPSlotCtrl: Any
    PXCAPSlotStatus: Any
    PXCAPRootCap: Any
    PXCAPRootCtrl: Any
    PXCAPRootStatus: Any
    PXCAPDevCap2: Any
    PXCAPDevCtrl2: Any
    PXCAPDevStatus2: Any
    PXCAPLinkCap2: Any
    PXCAPLinkCtrl2: Any
    PXCAPLinkStatus2: Any
    PXCAPSlotCap2: Any
    PXCAPSlotCtrl2: Any
    PXCAPSlotStatus2: Any
    sid: Any
    ssid: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class EtherDevice(PciEndpoint):
    BAR0: Any
    BAR1: Any
    BAR2: Any
    BAR3: Any
    BAR4: Any
    BAR5: Any
    CardbusCIS: Any
    SubsystemID: Any
    SubsystemVendorID: Any
    ExpansionROM: Any
    MaximumLatency: Any
    MinimumGrant: Any
    upstream: Any
    pci_dev: Any
    pci_func: Any
    pio_latency: Any
    config_latency: Any
    VendorID: Any
    DeviceID: Any
    Command: Any
    Status: Any
    Revision: Any
    ProgIF: Any
    SubClassCode: Any
    ClassCode: Any
    CacheLineSize: Any
    LatencyTimer: Any
    HeaderType: Any
    BIST: Any
    CapabilityPtr: Any
    InterruptLine: Any
    InterruptPin: Any
    PMCAPBaseOffset: Any
    PMCAPNextCapability: Any
    PMCAPCapId: Any
    PMCAPCapabilities: Any
    PMCAPCtrlStatus: Any
    MSICAPBaseOffset: Any
    MSICAPNextCapability: Any
    MSICAPCapId: Any
    MSICAPMsgCtrl: Any
    MSICAPMsgAddr: Any
    MSICAPMsgUpperAddr: Any
    MSICAPMsgData: Any
    MSICAPMaskBits: Any
    MSICAPPendingBits: Any
    MSIXCAPBaseOffset: Any
    MSIXCAPNextCapability: Any
    MSIXCAPCapId: Any
    MSIXMsgCtrl: Any
    MSIXTableOffset: Any
    MSIXPbaOffset: Any
    PXCAPBaseOffset: Any
    PXCAPNextCapability: Any
    PXCAPCapId: Any
    PXCAPCapabilities: Any
    PXCAPDevCapabilities: Any
    PXCAPDevCtrl: Any
    PXCAPDevStatus: Any
    PXCAPLinkCap: Any
    PXCAPLinkCtrl: Any
    PXCAPLinkStatus: Any
    PXCAPSlotCap: Any
    PXCAPSlotCtrl: Any
    PXCAPSlotStatus: Any
    PXCAPRootCap: Any
    PXCAPRootCtrl: Any
    PXCAPRootStatus: Any
    PXCAPDevCap2: Any
    PXCAPDevCtrl2: Any
    PXCAPDevStatus2: Any
    PXCAPLinkCap2: Any
    PXCAPLinkCtrl2: Any
    PXCAPLinkStatus2: Any
    PXCAPSlotCap2: Any
    PXCAPSlotCtrl2: Any
    PXCAPSlotStatus2: Any
    sid: Any
    ssid: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class EtherDump(SimObject):
    file: Any
    maxlen: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class EtherInt(Port):

    def __init__(self, *args, **kwargs) -> None: ...


class EtherLink(SimObject):
    delay: Any
    delay_var: Any
    speed: Any
    dump: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class EtherSwitch(SimObject):
    dump: Any
    fabric_speed: Any
    output_buffer_size: Any
    delay: Any
    delay_var: Any
    time_to_live: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class EtherTap(EtherTapBase):
    tun_clone_device: Any
    tap_device_name: Any
    bufsz: Any
    dump: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class EtherTapBase(SimObject):
    bufsz: Any
    dump: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class EtherTapStub(EtherTapBase):
    port: Any
    bufsz: Any
    dump: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class EthernetAddr(ParamValue):

    def __init__(self, *args, **kwargs) -> None: ...


class ExeTracer(InstTracer):
    disassembler: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class ExtCharacteristic(Enum):

    def __init__(self, *args, **kwargs) -> None: ...


class ExternalMaster(SimObject):
    port_type: Any
    port_data: Any
    system: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class ExternalSlave(SimObject):
    addr_ranges: Any
    port_type: Any
    port_data: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class FALRU(BaseTags):
    min_tracked_cache_size: Any
    system: Any
    size: Any
    block_size: Any
    tag_latency: Any
    warmup_percentage: Any
    sequential_access: Any
    indexing_policy: Any
    partitioning_manager: Any
    entry_size: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class FIFORP(BaseReplacementPolicy):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class FPC(BaseDictionaryCompressor):
    zero_run_bits: Any
    dictionary_size: Any
    block_size: Any
    chunk_size_bits: Any
    size_threshold_percentage: Any
    comp_chunks_per_cycle: Any
    comp_extra_latency: Any
    decomp_chunks_per_cycle: Any
    decomp_extra_latency: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class FPCD(BaseDictionaryCompressor):
    dictionary_size: Any
    block_size: Any
    chunk_size_bits: Any
    size_threshold_percentage: Any
    comp_chunks_per_cycle: Any
    comp_extra_latency: Any
    decomp_chunks_per_cycle: Any
    decomp_extra_latency: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class FP_ALU(FUDesc):
    count: Any
    opList: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class FP_MultDiv(FUDesc):
    count: Any
    opList: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class FUDesc(SimObject):
    count: Any
    opList: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class FUPool(SimObject):
    FUList: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class FaultModel(SimObject):
    baseline_fault_vector_database: Any
    temperature_weights_database: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Fdt(Fdt):

    def __init__(self, *args, **kwargs) -> None: ...


class FdtNode(FdtNode):

    def __init__(self, *args, **kwargs) -> None: ...


class FdtNop(FdtNop):

    def __init__(self, *args, **kwargs) -> None: ...


class FdtProperty(FdtProperty):

    def __init__(self, *args, **kwargs) -> None: ...


class FdtPropertyBytes(FdtPropertyBytes):

    def __init__(self, *args, **kwargs) -> None: ...


class FdtPropertyStrings(FdtPropertyStrings):

    def __init__(self, *args, **kwargs) -> None: ...


class FdtPropertyWords(FdtPropertyWords):

    def __init__(self, *args, **kwargs) -> None: ...


class FdtState:

    def __init__(self, *args, **kwargs) -> None: ...


class FetchDirectedPrefetcher(BasePrefetcher):
    cpu: Any
    latency: Any
    pfq_size: Any
    tq_size: Any
    mark_req_as_prefetch: Any
    squash_prefetches: Any
    cache_snoop: Any
    sys: Any
    block_size: Any
    on_miss: Any
    on_read: Any
    on_write: Any
    on_data: Any
    on_inst: Any
    prefetch_on_access: Any
    prefetch_on_pf_hit: Any
    use_virtual_addresses: Any
    page_bytes: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Float(ParamValue, float):

    def __init__(self, *args, **kwargs) -> None: ...


class Frequency(TickParamValue):

    def __init__(self, *args, **kwargs) -> None: ...


class FrequentValuesCompressor(BaseCacheCompressor):
    code_generation_ticks: Any
    counter_bits: Any
    max_code_length: Any
    num_samples: Any
    check_saturation: Any
    vft_assoc: Any
    vft_entries: Any
    vft_indexing_policy: Any
    vft_replacement_policy: Any
    block_size: Any
    chunk_size_bits: Any
    size_threshold_percentage: Any
    comp_chunks_per_cycle: Any
    comp_extra_latency: Any
    decomp_chunks_per_cycle: Any
    decomp_extra_latency: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class GDDR5_4000_2x32(DRAMInterface):
    page_policy: Any
    max_accesses_per_row: Any
    bank_groups_per_rank: Any
    enable_dram_powerdown: Any
    dll: Any
    tRCD: Any
    tRCD_WR: Any
    tCL: Any
    tCWL: Any
    tRP: Any
    tRAS: Any
    tWR: Any
    tRTP: Any
    tBURST_MAX: Any
    tBURST_MIN: Any
    tCCD_L: Any
    tCCD_L_WR: Any
    tRFC: Any
    tREFI: Any
    tWTR_L: Any
    tPPD: Any
    tAAD: Any
    two_cycle_activate: Any
    tRRD: Any
    tRRD_L: Any
    tXAW: Any
    activation_limit: Any
    tXP: Any
    tXPDLL: Any
    tXS: Any
    tXSDLL: Any
    beats_per_clock: Any
    data_clock_sync: Any
    IDD0: Any
    IDD02: Any
    IDD2P0: Any
    IDD2P02: Any
    IDD2P1: Any
    IDD2P12: Any
    IDD2N: Any
    IDD2N2: Any
    IDD3P0: Any
    IDD3P02: Any
    IDD3P1: Any
    IDD3P12: Any
    IDD3N: Any
    IDD3N2: Any
    IDD4R: Any
    IDD4R2: Any
    IDD4W: Any
    IDD4W2: Any
    IDD5: Any
    IDD52: Any
    IDD6: Any
    IDD62: Any
    VDD: Any
    VDD2: Any
    write_buffer_size: Any
    read_buffer_size: Any
    addr_mapping: Any
    device_size: Any
    device_bus_width: Any
    burst_length: Any
    device_rowbuffer_size: Any
    devices_per_rank: Any
    ranks_per_channel: Any
    banks_per_rank: Any
    tCK: Any
    tBURST: Any
    tWTR: Any
    tRTW: Any
    tCS: Any
    range: Any
    null: Any
    in_addr_map: Any
    kvm_map: Any
    conf_table_reported: Any
    image_file: Any
    writeable: Any
    collect_stats: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class GUPSGen(ClockedObject):
    system: Any
    start_addr: Any
    mem_size: Any
    update_limit: Any
    request_queue_size: Any
    init_memory: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class GarnetExtLink(BasicExtLink):
    network_links: Any
    credit_links: Any
    ext_cdc: Any
    int_cdc: Any
    ext_serdes: Any
    int_serdes: Any
    ext_net_bridge: Any
    ext_cred_bridge: Any
    int_net_bridge: Any
    int_cred_bridge: Any
    width: Any
    ext_node: Any
    int_node: Any
    link_id: Any
    latency: Any
    bandwidth_factor: Any
    weight: Any
    supported_vnets: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class GarnetIntLink(BasicIntLink):
    network_link: Any
    credit_link: Any
    src_cdc: Any
    dst_cdc: Any
    src_serdes: Any
    dst_serdes: Any
    src_net_bridge: Any
    dst_net_bridge: Any
    src_cred_bridge: Any
    dst_cred_bridge: Any
    width: Any
    src_node: Any
    dst_node: Any
    src_outport: Any
    dst_inport: Any
    link_id: Any
    latency: Any
    bandwidth_factor: Any
    weight: Any
    supported_vnets: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class GarnetNetwork(RubyNetwork):
    num_rows: Any
    ni_flit_size: Any
    vcs_per_vnet: Any
    buffers_per_data_vc: Any
    buffers_per_ctrl_vc: Any
    routing_algorithm: Any
    enable_fault_model: Any
    fault_model: Any
    garnet_deadlock_threshold: Any
    topology: Any
    number_of_virtual_networks: Any
    control_msg_size: Any
    ruby_system: Any
    routers: Any
    netifs: Any
    ext_links: Any
    int_links: Any
    data_msg_size: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class GarnetNetworkInterface(ClockedObject):
    id: Any
    vcs_per_vnet: Any
    virt_nets: Any
    garnet_deadlock_threshold: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class GarnetRouter(BasicRouter):
    vcs_per_vnet: Any
    virt_nets: Any
    width: Any
    router_id: Any
    latency: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class GarnetSyntheticTraffic(ClockedObject):
    block_offset: Any
    num_dest: Any
    memory_size: Any
    sim_cycles: Any
    num_packets_max: Any
    single_sender: Any
    single_dest: Any
    traffic_type: Any
    inj_rate: Any
    inj_vnet: Any
    precision: Any
    response_limit: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Gem5ToTlmBridge128(Gem5ToTlmBridgeBase):
    system: Any
    addr_ranges: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Gem5ToTlmBridge256(Gem5ToTlmBridgeBase):
    system: Any
    addr_ranges: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Gem5ToTlmBridge32(Gem5ToTlmBridgeBase):
    system: Any
    addr_ranges: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Gem5ToTlmBridge512(Gem5ToTlmBridgeBase):
    system: Any
    addr_ranges: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Gem5ToTlmBridge64(Gem5ToTlmBridgeBase):
    system: Any
    addr_ranges: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Gem5ToTlmBridgeBase(SystemC_ScModule):
    system: Any
    addr_ranges: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class GenericPciHost(PciHost):
    platform: Any
    conf_base: Any
    conf_size: Any
    conf_device_bits: Any
    pci_pio_base: Any
    pci_mem_base: Any
    pci_dma_base: Any
    up_to_down: Any
    down_to_up: Any
    config_error: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class GlobalInstTracker(SimObject):
    inst_thresholds: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class GoodbyeObject(SimObject):
    buffer_size: Any
    write_bandwidth: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class GshareBP(BranchPredictor):
    global_predictor_size: Any
    global_counter_bits: Any
    numThreads: Any
    instShiftAmt: Any
    speculativeHistUpdate: Any
    requiresBTBHit: Any
    updateBTBAtSquash: Any
    btb: Any
    ras: Any
    conditionalBranchPred: Any
    indirectBranchPred: Any
    takenOnlyHistory: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class HBMCtrl(MemCtrl):
    dram_2: Any
    dram: Any
    write_high_thresh_perc: Any
    write_low_thresh_perc: Any
    min_writes_per_switch: Any
    min_reads_per_switch: Any
    mem_sched_policy: Any
    static_frontend_latency: Any
    static_backend_latency: Any
    command_window: Any
    disable_sanity_check: Any
    system: Any
    qos_priorities: Any
    qos_policy: Any
    qos_turnaround_policy: Any
    qos_q_policy: Any
    qos_syncro_scheduler: Any
    qos_priority_escalation: Any
    qos_requestors: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class HBM_1000_4H_1x128(DRAMInterface):
    page_policy: Any
    max_accesses_per_row: Any
    bank_groups_per_rank: Any
    enable_dram_powerdown: Any
    dll: Any
    tRCD: Any
    tRCD_WR: Any
    tCL: Any
    tCWL: Any
    tRP: Any
    tRAS: Any
    tWR: Any
    tRTP: Any
    tBURST_MAX: Any
    tBURST_MIN: Any
    tCCD_L: Any
    tCCD_L_WR: Any
    tRFC: Any
    tREFI: Any
    tWTR_L: Any
    tPPD: Any
    tAAD: Any
    two_cycle_activate: Any
    tRRD: Any
    tRRD_L: Any
    tXAW: Any
    activation_limit: Any
    tXP: Any
    tXPDLL: Any
    tXS: Any
    tXSDLL: Any
    beats_per_clock: Any
    data_clock_sync: Any
    IDD0: Any
    IDD02: Any
    IDD2P0: Any
    IDD2P02: Any
    IDD2P1: Any
    IDD2P12: Any
    IDD2N: Any
    IDD2N2: Any
    IDD3P0: Any
    IDD3P02: Any
    IDD3P1: Any
    IDD3P12: Any
    IDD3N: Any
    IDD3N2: Any
    IDD4R: Any
    IDD4R2: Any
    IDD4W: Any
    IDD4W2: Any
    IDD5: Any
    IDD52: Any
    IDD6: Any
    IDD62: Any
    VDD: Any
    VDD2: Any
    write_buffer_size: Any
    read_buffer_size: Any
    addr_mapping: Any
    device_size: Any
    device_bus_width: Any
    burst_length: Any
    device_rowbuffer_size: Any
    devices_per_rank: Any
    ranks_per_channel: Any
    banks_per_rank: Any
    tCK: Any
    tBURST: Any
    tWTR: Any
    tRTW: Any
    tCS: Any
    range: Any
    null: Any
    in_addr_map: Any
    kvm_map: Any
    conf_table_reported: Any
    image_file: Any
    writeable: Any
    collect_stats: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class HBM_1000_4H_1x64(HBM_1000_4H_1x128):
    page_policy: Any
    max_accesses_per_row: Any
    bank_groups_per_rank: Any
    enable_dram_powerdown: Any
    dll: Any
    tRCD: Any
    tRCD_WR: Any
    tCL: Any
    tCWL: Any
    tRP: Any
    tRAS: Any
    tWR: Any
    tRTP: Any
    tBURST_MAX: Any
    tBURST_MIN: Any
    tCCD_L: Any
    tCCD_L_WR: Any
    tRFC: Any
    tREFI: Any
    tWTR_L: Any
    tPPD: Any
    tAAD: Any
    two_cycle_activate: Any
    tRRD: Any
    tRRD_L: Any
    tXAW: Any
    activation_limit: Any
    tXP: Any
    tXPDLL: Any
    tXS: Any
    tXSDLL: Any
    beats_per_clock: Any
    data_clock_sync: Any
    IDD0: Any
    IDD02: Any
    IDD2P0: Any
    IDD2P02: Any
    IDD2P1: Any
    IDD2P12: Any
    IDD2N: Any
    IDD2N2: Any
    IDD3P0: Any
    IDD3P02: Any
    IDD3P1: Any
    IDD3P12: Any
    IDD3N: Any
    IDD3N2: Any
    IDD4R: Any
    IDD4R2: Any
    IDD4W: Any
    IDD4W2: Any
    IDD5: Any
    IDD52: Any
    IDD6: Any
    IDD62: Any
    VDD: Any
    VDD2: Any
    write_buffer_size: Any
    read_buffer_size: Any
    addr_mapping: Any
    device_size: Any
    device_bus_width: Any
    burst_length: Any
    device_rowbuffer_size: Any
    devices_per_rank: Any
    ranks_per_channel: Any
    banks_per_rank: Any
    tCK: Any
    tBURST: Any
    tWTR: Any
    tRTW: Any
    tCS: Any
    range: Any
    null: Any
    in_addr_map: Any
    kvm_map: Any
    conf_table_reported: Any
    image_file: Any
    writeable: Any
    collect_stats: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class HBM_2000_4H_1x64(DRAMInterface):
    page_policy: Any
    max_accesses_per_row: Any
    bank_groups_per_rank: Any
    enable_dram_powerdown: Any
    dll: Any
    tRCD: Any
    tRCD_WR: Any
    tCL: Any
    tCWL: Any
    tRP: Any
    tRAS: Any
    tWR: Any
    tRTP: Any
    tBURST_MAX: Any
    tBURST_MIN: Any
    tCCD_L: Any
    tCCD_L_WR: Any
    tRFC: Any
    tREFI: Any
    tWTR_L: Any
    tPPD: Any
    tAAD: Any
    two_cycle_activate: Any
    tRRD: Any
    tRRD_L: Any
    tXAW: Any
    activation_limit: Any
    tXP: Any
    tXPDLL: Any
    tXS: Any
    tXSDLL: Any
    beats_per_clock: Any
    data_clock_sync: Any
    IDD0: Any
    IDD02: Any
    IDD2P0: Any
    IDD2P02: Any
    IDD2P1: Any
    IDD2P12: Any
    IDD2N: Any
    IDD2N2: Any
    IDD3P0: Any
    IDD3P02: Any
    IDD3P1: Any
    IDD3P12: Any
    IDD3N: Any
    IDD3N2: Any
    IDD4R: Any
    IDD4R2: Any
    IDD4W: Any
    IDD4W2: Any
    IDD5: Any
    IDD52: Any
    IDD6: Any
    IDD62: Any
    VDD: Any
    VDD2: Any
    write_buffer_size: Any
    read_buffer_size: Any
    addr_mapping: Any
    device_size: Any
    device_bus_width: Any
    burst_length: Any
    device_rowbuffer_size: Any
    devices_per_rank: Any
    ranks_per_channel: Any
    banks_per_rank: Any
    tCK: Any
    tBURST: Any
    tWTR: Any
    tRTW: Any
    tCS: Any
    range: Any
    null: Any
    in_addr_map: Any
    kvm_map: Any
    conf_table_reported: Any
    image_file: Any
    writeable: Any
    collect_stats: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class HMCController(NoncoherentXBar):
    frontend_latency: Any
    forward_latency: Any
    response_latency: Any
    header_latency: Any
    width: Any
    use_default_range: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class HMC_2500_1x32(DDR3_1600_8x8):
    page_policy: Any
    max_accesses_per_row: Any
    bank_groups_per_rank: Any
    enable_dram_powerdown: Any
    dll: Any
    tRCD: Any
    tRCD_WR: Any
    tCL: Any
    tCWL: Any
    tRP: Any
    tRAS: Any
    tWR: Any
    tRTP: Any
    tBURST_MAX: Any
    tBURST_MIN: Any
    tCCD_L: Any
    tCCD_L_WR: Any
    tRFC: Any
    tREFI: Any
    tWTR_L: Any
    tPPD: Any
    tAAD: Any
    two_cycle_activate: Any
    tRRD: Any
    tRRD_L: Any
    tXAW: Any
    activation_limit: Any
    tXP: Any
    tXPDLL: Any
    tXS: Any
    tXSDLL: Any
    beats_per_clock: Any
    data_clock_sync: Any
    IDD0: Any
    IDD02: Any
    IDD2P0: Any
    IDD2P02: Any
    IDD2P1: Any
    IDD2P12: Any
    IDD2N: Any
    IDD2N2: Any
    IDD3P0: Any
    IDD3P02: Any
    IDD3P1: Any
    IDD3P12: Any
    IDD3N: Any
    IDD3N2: Any
    IDD4R: Any
    IDD4R2: Any
    IDD4W: Any
    IDD4W2: Any
    IDD5: Any
    IDD52: Any
    IDD6: Any
    IDD62: Any
    VDD: Any
    VDD2: Any
    write_buffer_size: Any
    read_buffer_size: Any
    addr_mapping: Any
    device_size: Any
    device_bus_width: Any
    burst_length: Any
    device_rowbuffer_size: Any
    devices_per_rank: Any
    ranks_per_channel: Any
    banks_per_rank: Any
    tCK: Any
    tBURST: Any
    tWTR: Any
    tRTW: Any
    tCS: Any
    range: Any
    null: Any
    in_addr_map: Any
    kvm_map: Any
    conf_table_reported: Any
    image_file: Any
    writeable: Any
    collect_stats: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class HWPProbeEvent:

    def __init__(self, *args, **kwargs) -> None: ...


class HWPProbeEventRetiredInsts(HWPProbeEvent):

    def __init__(self, *args, **kwargs) -> None: ...


class HelloObject(SimObject):
    time_to_wait: Any
    number_of_fires: Any
    goodbye_object: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class HeteroMemCtrl(MemCtrl):
    nvm: Any
    dram: Any
    write_high_thresh_perc: Any
    write_low_thresh_perc: Any
    min_writes_per_switch: Any
    min_reads_per_switch: Any
    mem_sched_policy: Any
    static_frontend_latency: Any
    static_backend_latency: Any
    command_window: Any
    disable_sanity_check: Any
    system: Any
    qos_priorities: Any
    qos_policy: Any
    qos_turnaround_policy: Any
    qos_q_policy: Any
    qos_syncro_scheduler: Any
    qos_priority_escalation: Any
    qos_requestors: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class HostSocket(ParamValue):

    def __init__(self, *args, **kwargs) -> None: ...


class I2CBus(BasicPioDevice):
    devices: Any
    pio_addr: Any
    pio_latency: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class I2CDevice(SimObject):
    i2c_addr: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class I8042(PioDevice):
    pio_latency: Any
    data_port: Any
    command_port: Any
    keyboard: Any
    mouse: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class I82094AA(BasicPioDevice):
    apic_id: Any
    int_latency: Any
    pio_addr: Any
    pio_latency: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class I8237(BasicPioDevice):
    pio_addr: Any
    pio_latency: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class I8254(BasicPioDevice):
    pio_addr: Any
    pio_latency: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class I8259(BasicPioDevice):
    mode: Any
    slave: Any
    pio_addr: Any
    pio_latency: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class IGbE(EtherDevice):
    hardware_address: Any
    rx_fifo_size: Any
    tx_fifo_size: Any
    rx_desc_cache_size: Any
    tx_desc_cache_size: Any
    wb_delay: Any
    fetch_delay: Any
    fetch_comp_delay: Any
    wb_comp_delay: Any
    tx_read_delay: Any
    rx_write_delay: Any
    phy_pid: Any
    phy_epid: Any
    BAR0: Any
    BAR1: Any
    BAR2: Any
    BAR3: Any
    BAR4: Any
    BAR5: Any
    CardbusCIS: Any
    SubsystemID: Any
    SubsystemVendorID: Any
    ExpansionROM: Any
    MaximumLatency: Any
    MinimumGrant: Any
    upstream: Any
    pci_dev: Any
    pci_func: Any
    pio_latency: Any
    config_latency: Any
    VendorID: Any
    DeviceID: Any
    Command: Any
    Status: Any
    Revision: Any
    ProgIF: Any
    SubClassCode: Any
    ClassCode: Any
    CacheLineSize: Any
    LatencyTimer: Any
    HeaderType: Any
    BIST: Any
    CapabilityPtr: Any
    InterruptLine: Any
    InterruptPin: Any
    PMCAPBaseOffset: Any
    PMCAPNextCapability: Any
    PMCAPCapId: Any
    PMCAPCapabilities: Any
    PMCAPCtrlStatus: Any
    MSICAPBaseOffset: Any
    MSICAPNextCapability: Any
    MSICAPCapId: Any
    MSICAPMsgCtrl: Any
    MSICAPMsgAddr: Any
    MSICAPMsgUpperAddr: Any
    MSICAPMsgData: Any
    MSICAPMaskBits: Any
    MSICAPPendingBits: Any
    MSIXCAPBaseOffset: Any
    MSIXCAPNextCapability: Any
    MSIXCAPCapId: Any
    MSIXMsgCtrl: Any
    MSIXTableOffset: Any
    MSIXPbaOffset: Any
    PXCAPBaseOffset: Any
    PXCAPNextCapability: Any
    PXCAPCapId: Any
    PXCAPCapabilities: Any
    PXCAPDevCapabilities: Any
    PXCAPDevCtrl: Any
    PXCAPDevStatus: Any
    PXCAPLinkCap: Any
    PXCAPLinkCtrl: Any
    PXCAPLinkStatus: Any
    PXCAPSlotCap: Any
    PXCAPSlotCtrl: Any
    PXCAPSlotStatus: Any
    PXCAPRootCap: Any
    PXCAPRootCtrl: Any
    PXCAPRootStatus: Any
    PXCAPDevCap2: Any
    PXCAPDevCtrl2: Any
    PXCAPDevStatus2: Any
    PXCAPLinkCap2: Any
    PXCAPLinkCtrl2: Any
    PXCAPLinkStatus2: Any
    PXCAPSlotCap2: Any
    PXCAPSlotCtrl2: Any
    PXCAPSlotStatus2: Any
    sid: Any
    ssid: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class IGbE_e1000(IGbE):
    hardware_address: Any
    rx_fifo_size: Any
    tx_fifo_size: Any
    rx_desc_cache_size: Any
    tx_desc_cache_size: Any
    wb_delay: Any
    fetch_delay: Any
    fetch_comp_delay: Any
    wb_comp_delay: Any
    tx_read_delay: Any
    rx_write_delay: Any
    phy_pid: Any
    phy_epid: Any
    BAR0: Any
    BAR1: Any
    BAR2: Any
    BAR3: Any
    BAR4: Any
    BAR5: Any
    CardbusCIS: Any
    SubsystemID: Any
    SubsystemVendorID: Any
    ExpansionROM: Any
    MaximumLatency: Any
    MinimumGrant: Any
    upstream: Any
    pci_dev: Any
    pci_func: Any
    pio_latency: Any
    config_latency: Any
    VendorID: Any
    DeviceID: Any
    Command: Any
    Status: Any
    Revision: Any
    ProgIF: Any
    SubClassCode: Any
    ClassCode: Any
    CacheLineSize: Any
    LatencyTimer: Any
    HeaderType: Any
    BIST: Any
    CapabilityPtr: Any
    InterruptLine: Any
    InterruptPin: Any
    PMCAPBaseOffset: Any
    PMCAPNextCapability: Any
    PMCAPCapId: Any
    PMCAPCapabilities: Any
    PMCAPCtrlStatus: Any
    MSICAPBaseOffset: Any
    MSICAPNextCapability: Any
    MSICAPCapId: Any
    MSICAPMsgCtrl: Any
    MSICAPMsgAddr: Any
    MSICAPMsgUpperAddr: Any
    MSICAPMsgData: Any
    MSICAPMaskBits: Any
    MSICAPPendingBits: Any
    MSIXCAPBaseOffset: Any
    MSIXCAPNextCapability: Any
    MSIXCAPCapId: Any
    MSIXMsgCtrl: Any
    MSIXTableOffset: Any
    MSIXPbaOffset: Any
    PXCAPBaseOffset: Any
    PXCAPNextCapability: Any
    PXCAPCapId: Any
    PXCAPCapabilities: Any
    PXCAPDevCapabilities: Any
    PXCAPDevCtrl: Any
    PXCAPDevStatus: Any
    PXCAPLinkCap: Any
    PXCAPLinkCtrl: Any
    PXCAPLinkStatus: Any
    PXCAPSlotCap: Any
    PXCAPSlotCtrl: Any
    PXCAPSlotStatus: Any
    PXCAPRootCap: Any
    PXCAPRootCtrl: Any
    PXCAPRootStatus: Any
    PXCAPDevCap2: Any
    PXCAPDevCtrl2: Any
    PXCAPDevStatus2: Any
    PXCAPLinkCap2: Any
    PXCAPLinkCtrl2: Any
    PXCAPLinkStatus2: Any
    PXCAPSlotCap2: Any
    PXCAPSlotCtrl2: Any
    PXCAPSlotStatus2: Any
    sid: Any
    ssid: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class IGbE_igb(IGbE):
    hardware_address: Any
    rx_fifo_size: Any
    tx_fifo_size: Any
    rx_desc_cache_size: Any
    tx_desc_cache_size: Any
    wb_delay: Any
    fetch_delay: Any
    fetch_comp_delay: Any
    wb_comp_delay: Any
    tx_read_delay: Any
    rx_write_delay: Any
    phy_pid: Any
    phy_epid: Any
    BAR0: Any
    BAR1: Any
    BAR2: Any
    BAR3: Any
    BAR4: Any
    BAR5: Any
    CardbusCIS: Any
    SubsystemID: Any
    SubsystemVendorID: Any
    ExpansionROM: Any
    MaximumLatency: Any
    MinimumGrant: Any
    upstream: Any
    pci_dev: Any
    pci_func: Any
    pio_latency: Any
    config_latency: Any
    VendorID: Any
    DeviceID: Any
    Command: Any
    Status: Any
    Revision: Any
    ProgIF: Any
    SubClassCode: Any
    ClassCode: Any
    CacheLineSize: Any
    LatencyTimer: Any
    HeaderType: Any
    BIST: Any
    CapabilityPtr: Any
    InterruptLine: Any
    InterruptPin: Any
    PMCAPBaseOffset: Any
    PMCAPNextCapability: Any
    PMCAPCapId: Any
    PMCAPCapabilities: Any
    PMCAPCtrlStatus: Any
    MSICAPBaseOffset: Any
    MSICAPNextCapability: Any
    MSICAPCapId: Any
    MSICAPMsgCtrl: Any
    MSICAPMsgAddr: Any
    MSICAPMsgUpperAddr: Any
    MSICAPMsgData: Any
    MSICAPMaskBits: Any
    MSICAPPendingBits: Any
    MSIXCAPBaseOffset: Any
    MSIXCAPNextCapability: Any
    MSIXCAPCapId: Any
    MSIXMsgCtrl: Any
    MSIXTableOffset: Any
    MSIXPbaOffset: Any
    PXCAPBaseOffset: Any
    PXCAPNextCapability: Any
    PXCAPCapId: Any
    PXCAPCapabilities: Any
    PXCAPDevCapabilities: Any
    PXCAPDevCtrl: Any
    PXCAPDevStatus: Any
    PXCAPLinkCap: Any
    PXCAPLinkCtrl: Any
    PXCAPLinkStatus: Any
    PXCAPSlotCap: Any
    PXCAPSlotCtrl: Any
    PXCAPSlotStatus: Any
    PXCAPRootCap: Any
    PXCAPRootCtrl: Any
    PXCAPRootStatus: Any
    PXCAPDevCap2: Any
    PXCAPDevCtrl2: Any
    PXCAPDevStatus2: Any
    PXCAPLinkCap2: Any
    PXCAPLinkCtrl2: Any
    PXCAPLinkStatus2: Any
    PXCAPSlotCap2: Any
    PXCAPSlotCtrl2: Any
    PXCAPSlotStatus2: Any
    sid: Any
    ssid: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class IOXBar(NoncoherentXBar):
    frontend_latency: Any
    forward_latency: Any
    response_latency: Any
    header_latency: Any
    width: Any
    use_default_range: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class IQUnit(SimObject):
    numEntries: Any
    fuPool: Any
    numThreads: Any
    smtIQPolicy: Any
    smtIQThreshold: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class IdeController(PciEndpoint):
    disks: Any
    io_shift: Any
    ctrl_offset: Any
    BAR0: Any
    BAR1: Any
    BAR2: Any
    BAR3: Any
    BAR4: Any
    BAR5: Any
    CardbusCIS: Any
    SubsystemID: Any
    SubsystemVendorID: Any
    ExpansionROM: Any
    MaximumLatency: Any
    MinimumGrant: Any
    upstream: Any
    pci_dev: Any
    pci_func: Any
    pio_latency: Any
    config_latency: Any
    VendorID: Any
    DeviceID: Any
    Command: Any
    Status: Any
    Revision: Any
    ProgIF: Any
    SubClassCode: Any
    ClassCode: Any
    CacheLineSize: Any
    LatencyTimer: Any
    HeaderType: Any
    BIST: Any
    CapabilityPtr: Any
    InterruptLine: Any
    InterruptPin: Any
    PMCAPBaseOffset: Any
    PMCAPNextCapability: Any
    PMCAPCapId: Any
    PMCAPCapabilities: Any
    PMCAPCtrlStatus: Any
    MSICAPBaseOffset: Any
    MSICAPNextCapability: Any
    MSICAPCapId: Any
    MSICAPMsgCtrl: Any
    MSICAPMsgAddr: Any
    MSICAPMsgUpperAddr: Any
    MSICAPMsgData: Any
    MSICAPMaskBits: Any
    MSICAPPendingBits: Any
    MSIXCAPBaseOffset: Any
    MSIXCAPNextCapability: Any
    MSIXCAPCapId: Any
    MSIXMsgCtrl: Any
    MSIXTableOffset: Any
    MSIXPbaOffset: Any
    PXCAPBaseOffset: Any
    PXCAPNextCapability: Any
    PXCAPCapId: Any
    PXCAPCapabilities: Any
    PXCAPDevCapabilities: Any
    PXCAPDevCtrl: Any
    PXCAPDevStatus: Any
    PXCAPLinkCap: Any
    PXCAPLinkCtrl: Any
    PXCAPLinkStatus: Any
    PXCAPSlotCap: Any
    PXCAPSlotCtrl: Any
    PXCAPSlotStatus: Any
    PXCAPRootCap: Any
    PXCAPRootCtrl: Any
    PXCAPRootStatus: Any
    PXCAPDevCap2: Any
    PXCAPDevCtrl2: Any
    PXCAPDevStatus2: Any
    PXCAPLinkCap2: Any
    PXCAPLinkCtrl2: Any
    PXCAPLinkStatus2: Any
    PXCAPSlotCap2: Any
    PXCAPSlotCtrl2: Any
    PXCAPSlotStatus2: Any
    sid: Any
    ssid: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class IdeDisk(SimObject):
    delay: Any
    driveID: Any
    image: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class IdeID(Enum):

    def __init__(self, *args, **kwargs) -> None: ...


class ImageFormat(Enum):

    def __init__(self, *args, **kwargs) -> None: ...


class IndirectMemoryPrefetcher(QueuedPrefetcher):
    pt_table_entries: Any
    pt_table_assoc: Any
    pt_table_indexing_policy: Any
    pt_table_replacement_policy: Any
    max_prefetch_distance: Any
    num_indirect_counter_bits: Any
    ipd_table_entries: Any
    ipd_table_assoc: Any
    ipd_table_indexing_policy: Any
    ipd_table_replacement_policy: Any
    shift_values: Any
    addr_array_len: Any
    prefetch_threshold: Any
    stream_counter_threshold: Any
    streaming_distance: Any
    latency: Any
    queue_size: Any
    max_prefetch_requests_with_pending_translation: Any
    queue_squash: Any
    queue_filter: Any
    cache_snoop: Any
    tag_prefetch: Any
    throttle_control_percentage: Any
    sys: Any
    block_size: Any
    on_miss: Any
    on_read: Any
    on_write: Any
    on_data: Any
    on_inst: Any
    prefetch_on_access: Any
    prefetch_on_pf_hit: Any
    use_virtual_addresses: Any
    page_bytes: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class IndirectPredictor(SimObject):
    numThreads: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class InstDecoder(SimObject):
    isa: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class InstDisassembler(SimObject):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class InstPBTrace(InstTracer):
    file_name: Any
    disassembler: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class InstTracer(SimObject):
    disassembler: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Int(CheckedInt):

    def __init__(self, *args, **kwargs) -> None: ...


class Int16(CheckedInt):

    def __init__(self, *args, **kwargs) -> None: ...


class Int32(CheckedInt):

    def __init__(self, *args, **kwargs) -> None: ...


class Int64(CheckedInt):

    def __init__(self, *args, **kwargs) -> None: ...


class Int8(CheckedInt):

    def __init__(self, *args, **kwargs) -> None: ...


class IntALU(FUDesc):
    count: Any
    opList: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class IntMultDiv(FUDesc):
    count: Any
    opList: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class IntSinkPin(Port):

    def __init__(self, *args, **kwargs) -> None: ...


class IntSourcePin(VectorPort):

    def __init__(self, *args, **kwargs) -> None: ...


class IntelTrace(InstTracer):
    disassembler: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class InvalidateGenerator(DirectedGenerator):
    addr_increment_size: Any
    num_cpus: Any
    system: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class IpAddress(ParamValue):

    def __init__(self, *args, **kwargs) -> None: ...


class IpNetmask(IpAddress):

    def __init__(self, *args, **kwargs) -> None: ...


class IpWithPort(IpAddress):

    def __init__(self, *args, **kwargs) -> None: ...


class IrregularStreamBufferPrefetcher(QueuedPrefetcher):
    num_counter_bits: Any
    chunk_size: Any
    degree: Any
    training_unit_assoc: Any
    training_unit_entries: Any
    training_unit_indexing_policy: Any
    training_unit_replacement_policy: Any
    prefetch_candidates_per_entry: Any
    address_map_cache_assoc: Any
    address_map_cache_entries: Any
    ps_address_map_cache_indexing_policy: Any
    ps_address_map_cache_replacement_policy: Any
    sp_address_map_cache_indexing_policy: Any
    sp_address_map_cache_replacement_policy: Any
    latency: Any
    queue_size: Any
    max_prefetch_requests_with_pending_translation: Any
    queue_squash: Any
    queue_filter: Any
    cache_snoop: Any
    tag_prefetch: Any
    throttle_control_percentage: Any
    sys: Any
    block_size: Any
    on_miss: Any
    on_read: Any
    on_write: Any
    on_data: Any
    on_inst: Any
    prefetch_on_access: Any
    prefetch_on_pf_hit: Any
    use_virtual_addresses: Any
    page_bytes: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class IsaFake(BasicPioDevice):
    pio_size: Any
    ret_data8: Any
    ret_data16: Any
    ret_data32: Any
    ret_data64: Any
    ret_bad_addr: Any
    update_data: Any
    warn_access: Any
    fake_mem: Any
    pio_addr: Any
    pio_latency: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class KernelPanicOopsBehaviour(ScopedEnum):

    def __init__(self, *args, **kwargs) -> None: ...


class KernelWorkload(Workload):
    object_file: Any
    extras: Any
    extras_addrs: Any
    addr_check: Any
    load_addr_mask: Any
    load_addr_offset: Any
    command_line: Any
    on_panic: Any
    on_oops: Any
    wait_for_remote_gdb: Any
    remote_gdb_port: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class KvmVM(SimObject):
    coalescedMMIO: Any
    system: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class L1Cache_Controller(MESI_Two_Level_L1Cache_Controller):
    sequencer: Any
    L1Icache: Any
    L1Dcache: Any
    prefetcher: Any
    l2_select_num_bits: Any
    l1_request_latency: Any
    l1_response_latency: Any
    to_l2_latency: Any
    llsc_lock_timeout_latency: Any
    use_llsc_lock: Any
    send_evictions: Any
    enable_prefetch: Any
    requestFromL1Cache: Any
    responseFromL1Cache: Any
    unblockFromL1Cache: Any
    requestToL1Cache: Any
    responseToL1Cache: Any
    optionalQueue: Any
    mandatoryQueue: Any
    version: Any
    addr_ranges: Any
    cluster_id: Any
    transitions_per_cycle: Any
    buffer_size: Any
    recycle_latency: Any
    number_of_TBEs: Any
    ruby_system: Any
    mandatory_queue_latency: Any
    system: Any
    upstream_destinations: Any
    downstream_destinations: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class L2Cache_Controller(MESI_Two_Level_L2Cache_Controller):
    L2cache: Any
    l2_request_latency: Any
    l2_response_latency: Any
    to_l1_latency: Any
    DirRequestFromL2Cache: Any
    L1RequestFromL2Cache: Any
    responseFromL2Cache: Any
    unblockToL2Cache: Any
    L1RequestToL2Cache: Any
    responseToL2Cache: Any
    version: Any
    addr_ranges: Any
    cluster_id: Any
    transitions_per_cycle: Any
    buffer_size: Any
    recycle_latency: Any
    number_of_TBEs: Any
    ruby_system: Any
    mandatory_queue_latency: Any
    system: Any
    upstream_destinations: Any
    downstream_destinations: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class L2XBar(CoherentXBar):
    snoop_response_latency: Any
    snoop_filter: Any
    max_outstanding_snoops: Any
    max_routing_table_size: Any
    point_of_coherency: Any
    point_of_unification: Any
    system: Any
    frontend_latency: Any
    forward_latency: Any
    response_latency: Any
    header_latency: Any
    width: Any
    use_default_range: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class LFURP(BaseReplacementPolicy):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class LIPRP(BIPRP):
    btp: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class LPDDR2_S4_1066_1x32(DRAMInterface):
    page_policy: Any
    max_accesses_per_row: Any
    bank_groups_per_rank: Any
    enable_dram_powerdown: Any
    dll: Any
    tRCD: Any
    tRCD_WR: Any
    tCL: Any
    tCWL: Any
    tRP: Any
    tRAS: Any
    tWR: Any
    tRTP: Any
    tBURST_MAX: Any
    tBURST_MIN: Any
    tCCD_L: Any
    tCCD_L_WR: Any
    tRFC: Any
    tREFI: Any
    tWTR_L: Any
    tPPD: Any
    tAAD: Any
    two_cycle_activate: Any
    tRRD: Any
    tRRD_L: Any
    tXAW: Any
    activation_limit: Any
    tXP: Any
    tXPDLL: Any
    tXS: Any
    tXSDLL: Any
    beats_per_clock: Any
    data_clock_sync: Any
    IDD0: Any
    IDD02: Any
    IDD2P0: Any
    IDD2P02: Any
    IDD2P1: Any
    IDD2P12: Any
    IDD2N: Any
    IDD2N2: Any
    IDD3P0: Any
    IDD3P02: Any
    IDD3P1: Any
    IDD3P12: Any
    IDD3N: Any
    IDD3N2: Any
    IDD4R: Any
    IDD4R2: Any
    IDD4W: Any
    IDD4W2: Any
    IDD5: Any
    IDD52: Any
    IDD6: Any
    IDD62: Any
    VDD: Any
    VDD2: Any
    write_buffer_size: Any
    read_buffer_size: Any
    addr_mapping: Any
    device_size: Any
    device_bus_width: Any
    burst_length: Any
    device_rowbuffer_size: Any
    devices_per_rank: Any
    ranks_per_channel: Any
    banks_per_rank: Any
    tCK: Any
    tBURST: Any
    tWTR: Any
    tRTW: Any
    tCS: Any
    range: Any
    null: Any
    in_addr_map: Any
    kvm_map: Any
    conf_table_reported: Any
    image_file: Any
    writeable: Any
    collect_stats: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class LPDDR3_1600_1x32(DRAMInterface):
    page_policy: Any
    max_accesses_per_row: Any
    bank_groups_per_rank: Any
    enable_dram_powerdown: Any
    dll: Any
    tRCD: Any
    tRCD_WR: Any
    tCL: Any
    tCWL: Any
    tRP: Any
    tRAS: Any
    tWR: Any
    tRTP: Any
    tBURST_MAX: Any
    tBURST_MIN: Any
    tCCD_L: Any
    tCCD_L_WR: Any
    tRFC: Any
    tREFI: Any
    tWTR_L: Any
    tPPD: Any
    tAAD: Any
    two_cycle_activate: Any
    tRRD: Any
    tRRD_L: Any
    tXAW: Any
    activation_limit: Any
    tXP: Any
    tXPDLL: Any
    tXS: Any
    tXSDLL: Any
    beats_per_clock: Any
    data_clock_sync: Any
    IDD0: Any
    IDD02: Any
    IDD2P0: Any
    IDD2P02: Any
    IDD2P1: Any
    IDD2P12: Any
    IDD2N: Any
    IDD2N2: Any
    IDD3P0: Any
    IDD3P02: Any
    IDD3P1: Any
    IDD3P12: Any
    IDD3N: Any
    IDD3N2: Any
    IDD4R: Any
    IDD4R2: Any
    IDD4W: Any
    IDD4W2: Any
    IDD5: Any
    IDD52: Any
    IDD6: Any
    IDD62: Any
    VDD: Any
    VDD2: Any
    write_buffer_size: Any
    read_buffer_size: Any
    addr_mapping: Any
    device_size: Any
    device_bus_width: Any
    burst_length: Any
    device_rowbuffer_size: Any
    devices_per_rank: Any
    ranks_per_channel: Any
    banks_per_rank: Any
    tCK: Any
    tBURST: Any
    tWTR: Any
    tRTW: Any
    tCS: Any
    range: Any
    null: Any
    in_addr_map: Any
    kvm_map: Any
    conf_table_reported: Any
    image_file: Any
    writeable: Any
    collect_stats: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class LPDDR5_5500_1x16_8B_BL32(LPDDR5_5500_1x16_BG_BL32):
    page_policy: Any
    max_accesses_per_row: Any
    bank_groups_per_rank: Any
    enable_dram_powerdown: Any
    dll: Any
    tRCD: Any
    tRCD_WR: Any
    tCL: Any
    tCWL: Any
    tRP: Any
    tRAS: Any
    tWR: Any
    tRTP: Any
    tBURST_MAX: Any
    tBURST_MIN: Any
    tCCD_L: Any
    tCCD_L_WR: Any
    tRFC: Any
    tREFI: Any
    tWTR_L: Any
    tPPD: Any
    tAAD: Any
    two_cycle_activate: Any
    tRRD: Any
    tRRD_L: Any
    tXAW: Any
    activation_limit: Any
    tXP: Any
    tXPDLL: Any
    tXS: Any
    tXSDLL: Any
    beats_per_clock: Any
    data_clock_sync: Any
    IDD0: Any
    IDD02: Any
    IDD2P0: Any
    IDD2P02: Any
    IDD2P1: Any
    IDD2P12: Any
    IDD2N: Any
    IDD2N2: Any
    IDD3P0: Any
    IDD3P02: Any
    IDD3P1: Any
    IDD3P12: Any
    IDD3N: Any
    IDD3N2: Any
    IDD4R: Any
    IDD4R2: Any
    IDD4W: Any
    IDD4W2: Any
    IDD5: Any
    IDD52: Any
    IDD6: Any
    IDD62: Any
    VDD: Any
    VDD2: Any
    write_buffer_size: Any
    read_buffer_size: Any
    addr_mapping: Any
    device_size: Any
    device_bus_width: Any
    burst_length: Any
    device_rowbuffer_size: Any
    devices_per_rank: Any
    ranks_per_channel: Any
    banks_per_rank: Any
    tCK: Any
    tBURST: Any
    tWTR: Any
    tRTW: Any
    tCS: Any
    range: Any
    null: Any
    in_addr_map: Any
    kvm_map: Any
    conf_table_reported: Any
    image_file: Any
    writeable: Any
    collect_stats: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class LPDDR5_5500_1x16_BG_BL16(LPDDR5_5500_1x16_BG_BL32):
    page_policy: Any
    max_accesses_per_row: Any
    bank_groups_per_rank: Any
    enable_dram_powerdown: Any
    dll: Any
    tRCD: Any
    tRCD_WR: Any
    tCL: Any
    tCWL: Any
    tRP: Any
    tRAS: Any
    tWR: Any
    tRTP: Any
    tBURST_MAX: Any
    tBURST_MIN: Any
    tCCD_L: Any
    tCCD_L_WR: Any
    tRFC: Any
    tREFI: Any
    tWTR_L: Any
    tPPD: Any
    tAAD: Any
    two_cycle_activate: Any
    tRRD: Any
    tRRD_L: Any
    tXAW: Any
    activation_limit: Any
    tXP: Any
    tXPDLL: Any
    tXS: Any
    tXSDLL: Any
    beats_per_clock: Any
    data_clock_sync: Any
    IDD0: Any
    IDD02: Any
    IDD2P0: Any
    IDD2P02: Any
    IDD2P1: Any
    IDD2P12: Any
    IDD2N: Any
    IDD2N2: Any
    IDD3P0: Any
    IDD3P02: Any
    IDD3P1: Any
    IDD3P12: Any
    IDD3N: Any
    IDD3N2: Any
    IDD4R: Any
    IDD4R2: Any
    IDD4W: Any
    IDD4W2: Any
    IDD5: Any
    IDD52: Any
    IDD6: Any
    IDD62: Any
    VDD: Any
    VDD2: Any
    write_buffer_size: Any
    read_buffer_size: Any
    addr_mapping: Any
    device_size: Any
    device_bus_width: Any
    burst_length: Any
    device_rowbuffer_size: Any
    devices_per_rank: Any
    ranks_per_channel: Any
    banks_per_rank: Any
    tCK: Any
    tBURST: Any
    tWTR: Any
    tRTW: Any
    tCS: Any
    range: Any
    null: Any
    in_addr_map: Any
    kvm_map: Any
    conf_table_reported: Any
    image_file: Any
    writeable: Any
    collect_stats: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class LPDDR5_5500_1x16_BG_BL32(DRAMInterface):
    page_policy: Any
    max_accesses_per_row: Any
    bank_groups_per_rank: Any
    enable_dram_powerdown: Any
    dll: Any
    tRCD: Any
    tRCD_WR: Any
    tCL: Any
    tCWL: Any
    tRP: Any
    tRAS: Any
    tWR: Any
    tRTP: Any
    tBURST_MAX: Any
    tBURST_MIN: Any
    tCCD_L: Any
    tCCD_L_WR: Any
    tRFC: Any
    tREFI: Any
    tWTR_L: Any
    tPPD: Any
    tAAD: Any
    two_cycle_activate: Any
    tRRD: Any
    tRRD_L: Any
    tXAW: Any
    activation_limit: Any
    tXP: Any
    tXPDLL: Any
    tXS: Any
    tXSDLL: Any
    beats_per_clock: Any
    data_clock_sync: Any
    IDD0: Any
    IDD02: Any
    IDD2P0: Any
    IDD2P02: Any
    IDD2P1: Any
    IDD2P12: Any
    IDD2N: Any
    IDD2N2: Any
    IDD3P0: Any
    IDD3P02: Any
    IDD3P1: Any
    IDD3P12: Any
    IDD3N: Any
    IDD3N2: Any
    IDD4R: Any
    IDD4R2: Any
    IDD4W: Any
    IDD4W2: Any
    IDD5: Any
    IDD52: Any
    IDD6: Any
    IDD62: Any
    VDD: Any
    VDD2: Any
    write_buffer_size: Any
    read_buffer_size: Any
    addr_mapping: Any
    device_size: Any
    device_bus_width: Any
    burst_length: Any
    device_rowbuffer_size: Any
    devices_per_rank: Any
    ranks_per_channel: Any
    banks_per_rank: Any
    tCK: Any
    tBURST: Any
    tWTR: Any
    tRTW: Any
    tCS: Any
    range: Any
    null: Any
    in_addr_map: Any
    kvm_map: Any
    conf_table_reported: Any
    image_file: Any
    writeable: Any
    collect_stats: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class LPDDR5_6400_1x16_8B_BL32(LPDDR5_6400_1x16_BG_BL32):
    page_policy: Any
    max_accesses_per_row: Any
    bank_groups_per_rank: Any
    enable_dram_powerdown: Any
    dll: Any
    tRCD: Any
    tRCD_WR: Any
    tCL: Any
    tCWL: Any
    tRP: Any
    tRAS: Any
    tWR: Any
    tRTP: Any
    tBURST_MAX: Any
    tBURST_MIN: Any
    tCCD_L: Any
    tCCD_L_WR: Any
    tRFC: Any
    tREFI: Any
    tWTR_L: Any
    tPPD: Any
    tAAD: Any
    two_cycle_activate: Any
    tRRD: Any
    tRRD_L: Any
    tXAW: Any
    activation_limit: Any
    tXP: Any
    tXPDLL: Any
    tXS: Any
    tXSDLL: Any
    beats_per_clock: Any
    data_clock_sync: Any
    IDD0: Any
    IDD02: Any
    IDD2P0: Any
    IDD2P02: Any
    IDD2P1: Any
    IDD2P12: Any
    IDD2N: Any
    IDD2N2: Any
    IDD3P0: Any
    IDD3P02: Any
    IDD3P1: Any
    IDD3P12: Any
    IDD3N: Any
    IDD3N2: Any
    IDD4R: Any
    IDD4R2: Any
    IDD4W: Any
    IDD4W2: Any
    IDD5: Any
    IDD52: Any
    IDD6: Any
    IDD62: Any
    VDD: Any
    VDD2: Any
    write_buffer_size: Any
    read_buffer_size: Any
    addr_mapping: Any
    device_size: Any
    device_bus_width: Any
    burst_length: Any
    device_rowbuffer_size: Any
    devices_per_rank: Any
    ranks_per_channel: Any
    banks_per_rank: Any
    tCK: Any
    tBURST: Any
    tWTR: Any
    tRTW: Any
    tCS: Any
    range: Any
    null: Any
    in_addr_map: Any
    kvm_map: Any
    conf_table_reported: Any
    image_file: Any
    writeable: Any
    collect_stats: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class LPDDR5_6400_1x16_BG_BL16(LPDDR5_6400_1x16_BG_BL32):
    page_policy: Any
    max_accesses_per_row: Any
    bank_groups_per_rank: Any
    enable_dram_powerdown: Any
    dll: Any
    tRCD: Any
    tRCD_WR: Any
    tCL: Any
    tCWL: Any
    tRP: Any
    tRAS: Any
    tWR: Any
    tRTP: Any
    tBURST_MAX: Any
    tBURST_MIN: Any
    tCCD_L: Any
    tCCD_L_WR: Any
    tRFC: Any
    tREFI: Any
    tWTR_L: Any
    tPPD: Any
    tAAD: Any
    two_cycle_activate: Any
    tRRD: Any
    tRRD_L: Any
    tXAW: Any
    activation_limit: Any
    tXP: Any
    tXPDLL: Any
    tXS: Any
    tXSDLL: Any
    beats_per_clock: Any
    data_clock_sync: Any
    IDD0: Any
    IDD02: Any
    IDD2P0: Any
    IDD2P02: Any
    IDD2P1: Any
    IDD2P12: Any
    IDD2N: Any
    IDD2N2: Any
    IDD3P0: Any
    IDD3P02: Any
    IDD3P1: Any
    IDD3P12: Any
    IDD3N: Any
    IDD3N2: Any
    IDD4R: Any
    IDD4R2: Any
    IDD4W: Any
    IDD4W2: Any
    IDD5: Any
    IDD52: Any
    IDD6: Any
    IDD62: Any
    VDD: Any
    VDD2: Any
    write_buffer_size: Any
    read_buffer_size: Any
    addr_mapping: Any
    device_size: Any
    device_bus_width: Any
    burst_length: Any
    device_rowbuffer_size: Any
    devices_per_rank: Any
    ranks_per_channel: Any
    banks_per_rank: Any
    tCK: Any
    tBURST: Any
    tWTR: Any
    tRTW: Any
    tCS: Any
    range: Any
    null: Any
    in_addr_map: Any
    kvm_map: Any
    conf_table_reported: Any
    image_file: Any
    writeable: Any
    collect_stats: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class LPDDR5_6400_1x16_BG_BL32(LPDDR5_5500_1x16_BG_BL32):
    page_policy: Any
    max_accesses_per_row: Any
    bank_groups_per_rank: Any
    enable_dram_powerdown: Any
    dll: Any
    tRCD: Any
    tRCD_WR: Any
    tCL: Any
    tCWL: Any
    tRP: Any
    tRAS: Any
    tWR: Any
    tRTP: Any
    tBURST_MAX: Any
    tBURST_MIN: Any
    tCCD_L: Any
    tCCD_L_WR: Any
    tRFC: Any
    tREFI: Any
    tWTR_L: Any
    tPPD: Any
    tAAD: Any
    two_cycle_activate: Any
    tRRD: Any
    tRRD_L: Any
    tXAW: Any
    activation_limit: Any
    tXP: Any
    tXPDLL: Any
    tXS: Any
    tXSDLL: Any
    beats_per_clock: Any
    data_clock_sync: Any
    IDD0: Any
    IDD02: Any
    IDD2P0: Any
    IDD2P02: Any
    IDD2P1: Any
    IDD2P12: Any
    IDD2N: Any
    IDD2N2: Any
    IDD3P0: Any
    IDD3P02: Any
    IDD3P1: Any
    IDD3P12: Any
    IDD3N: Any
    IDD3N2: Any
    IDD4R: Any
    IDD4R2: Any
    IDD4W: Any
    IDD4W2: Any
    IDD5: Any
    IDD52: Any
    IDD6: Any
    IDD62: Any
    VDD: Any
    VDD2: Any
    write_buffer_size: Any
    read_buffer_size: Any
    addr_mapping: Any
    device_size: Any
    device_bus_width: Any
    burst_length: Any
    device_rowbuffer_size: Any
    devices_per_rank: Any
    ranks_per_channel: Any
    banks_per_rank: Any
    tCK: Any
    tBURST: Any
    tWTR: Any
    tRTW: Any
    tCS: Any
    range: Any
    null: Any
    in_addr_map: Any
    kvm_map: Any
    conf_table_reported: Any
    image_file: Any
    writeable: Any
    collect_stats: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class LRURP(BaseReplacementPolicy):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class LTAGE(TAGE):
    loop_predictor: Any
    tage: Any
    numThreads: Any
    instShiftAmt: Any
    speculativeHistUpdate: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class LTAGE_TAGE(TAGEBase):
    numThreads: Any
    instShiftAmt: Any
    nHistoryTables: Any
    minHist: Any
    maxHist: Any
    tagTableTagWidths: Any
    logTagTableSizes: Any
    logRatioBiModalHystEntries: Any
    tagTableCounterBits: Any
    tagTableUBits: Any
    histBufferSize: Any
    pathHistBits: Any
    logUResetPeriod: Any
    numUseAltOnNa: Any
    initialTCounterValue: Any
    useAltOnNaBits: Any
    maxNumAlloc: Any
    noSkip: Any
    speculativeHistUpdate: Any
    takenOnlyHistory: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Latency(TickParamValue):

    def __init__(self, *args, **kwargs) -> None: ...


class LocalBP(ConditionalPredictor):
    localPredictorSize: Any
    localCtrBits: Any
    numThreads: Any
    instShiftAmt: Any
    speculativeHistUpdate: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class LocalInstTracker(ProbeListenerObject):
    global_inst_tracker: Any
    start_listening: Any
    manager: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class LoopPredictor(SimObject):
    logSizeLoopPred: Any
    withLoopBits: Any
    loopTableAgeBits: Any
    loopTableConfidenceBits: Any
    loopTableTagBits: Any
    loopTableIterBits: Any
    logLoopTableAssoc: Any
    useSpeculation: Any
    useHashing: Any
    useDirectionBit: Any
    restrictAllocation: Any
    initialLoopIter: Any
    initialLoopAge: Any
    optionalAgeReset: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class LooppointAnalysis(ProbeListenerObject):
    looppoint_analysis_manager: Any
    bb_valid_addr_range: Any
    marker_valid_addr_range: Any
    bb_excluded_addr_ranges: Any
    if_listening: Any
    manager: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class LooppointAnalysisManager(SimObject):
    region_length: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MESI_Two_Level_DMA_Controller(RubyController):
    dma_sequencer: Any
    request_latency: Any
    responseFromDir: Any
    requestToDir: Any
    mandatoryQueue: Any
    version: Any
    addr_ranges: Any
    cluster_id: Any
    transitions_per_cycle: Any
    buffer_size: Any
    recycle_latency: Any
    number_of_TBEs: Any
    ruby_system: Any
    mandatory_queue_latency: Any
    system: Any
    upstream_destinations: Any
    downstream_destinations: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MESI_Two_Level_Directory_Controller(RubyController):
    directory: Any
    to_mem_ctrl_latency: Any
    directory_latency: Any
    requestToDir: Any
    responseToDir: Any
    responseFromDir: Any
    requestToMemory: Any
    responseFromMemory: Any
    version: Any
    addr_ranges: Any
    cluster_id: Any
    transitions_per_cycle: Any
    buffer_size: Any
    recycle_latency: Any
    number_of_TBEs: Any
    ruby_system: Any
    mandatory_queue_latency: Any
    system: Any
    upstream_destinations: Any
    downstream_destinations: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MESI_Two_Level_L1Cache_Controller(RubyController):
    sequencer: Any
    L1Icache: Any
    L1Dcache: Any
    prefetcher: Any
    l2_select_num_bits: Any
    l1_request_latency: Any
    l1_response_latency: Any
    to_l2_latency: Any
    llsc_lock_timeout_latency: Any
    use_llsc_lock: Any
    send_evictions: Any
    enable_prefetch: Any
    requestFromL1Cache: Any
    responseFromL1Cache: Any
    unblockFromL1Cache: Any
    requestToL1Cache: Any
    responseToL1Cache: Any
    optionalQueue: Any
    mandatoryQueue: Any
    version: Any
    addr_ranges: Any
    cluster_id: Any
    transitions_per_cycle: Any
    buffer_size: Any
    recycle_latency: Any
    number_of_TBEs: Any
    ruby_system: Any
    mandatory_queue_latency: Any
    system: Any
    upstream_destinations: Any
    downstream_destinations: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MESI_Two_Level_L2Cache_Controller(RubyController):
    L2cache: Any
    l2_request_latency: Any
    l2_response_latency: Any
    to_l1_latency: Any
    DirRequestFromL2Cache: Any
    L1RequestFromL2Cache: Any
    responseFromL2Cache: Any
    unblockToL2Cache: Any
    L1RequestToL2Cache: Any
    responseToL2Cache: Any
    version: Any
    addr_ranges: Any
    cluster_id: Any
    transitions_per_cycle: Any
    buffer_size: Any
    recycle_latency: Any
    number_of_TBEs: Any
    ruby_system: Any
    mandatory_queue_latency: Any
    system: Any
    upstream_destinations: Any
    downstream_destinations: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MPP_LoopPredictor(LoopPredictor):
    logSizeLoopPred: Any
    withLoopBits: Any
    loopTableAgeBits: Any
    loopTableConfidenceBits: Any
    loopTableTagBits: Any
    loopTableIterBits: Any
    logLoopTableAssoc: Any
    useSpeculation: Any
    useHashing: Any
    useDirectionBit: Any
    restrictAllocation: Any
    initialLoopIter: Any
    initialLoopAge: Any
    optionalAgeReset: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MPP_LoopPredictor_8KB(MPP_LoopPredictor):
    logSizeLoopPred: Any
    withLoopBits: Any
    loopTableAgeBits: Any
    loopTableConfidenceBits: Any
    loopTableTagBits: Any
    loopTableIterBits: Any
    logLoopTableAssoc: Any
    useSpeculation: Any
    useHashing: Any
    useDirectionBit: Any
    restrictAllocation: Any
    initialLoopIter: Any
    initialLoopAge: Any
    optionalAgeReset: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MPP_StatisticalCorrector(StatisticalCorrector):
    gnb: Any
    gm: Any
    logGnb: Any
    pnb: Any
    pm: Any
    logPnb: Any
    instShiftAmt: Any
    numEntriesFirstLocalHistories: Any
    bwnb: Any
    bwm: Any
    logBwnb: Any
    bwWeightInitValue: Any
    lnb: Any
    lm: Any
    logLnb: Any
    lWeightInitValue: Any
    inb: Any
    im: Any
    logInb: Any
    iWeightInitValue: Any
    logBias: Any
    logSizeUp: Any
    chooserConfWidth: Any
    updateThresholdWidth: Any
    pUpdateThresholdWidth: Any
    extraWeightsWidth: Any
    scCountersWidth: Any
    initialUpdateThresholdValue: Any
    speculativeHistUpdate: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MPP_StatisticalCorrector_64KB(MPP_StatisticalCorrector):
    snb: Any
    sm: Any
    logSnb: Any
    tnb: Any
    tm: Any
    logTnb: Any
    numEntriesSecondLocalHistories: Any
    numEntriesThirdLocalHistories: Any
    gnb: Any
    gm: Any
    logGnb: Any
    pnb: Any
    pm: Any
    logPnb: Any
    instShiftAmt: Any
    numEntriesFirstLocalHistories: Any
    bwnb: Any
    bwm: Any
    logBwnb: Any
    bwWeightInitValue: Any
    lnb: Any
    lm: Any
    logLnb: Any
    lWeightInitValue: Any
    inb: Any
    im: Any
    logInb: Any
    iWeightInitValue: Any
    logBias: Any
    logSizeUp: Any
    chooserConfWidth: Any
    updateThresholdWidth: Any
    pUpdateThresholdWidth: Any
    extraWeightsWidth: Any
    scCountersWidth: Any
    initialUpdateThresholdValue: Any
    speculativeHistUpdate: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MPP_StatisticalCorrector_8KB(MPP_StatisticalCorrector):
    gnb: Any
    gm: Any
    logGnb: Any
    pnb: Any
    pm: Any
    logPnb: Any
    instShiftAmt: Any
    numEntriesFirstLocalHistories: Any
    bwnb: Any
    bwm: Any
    logBwnb: Any
    bwWeightInitValue: Any
    lnb: Any
    lm: Any
    logLnb: Any
    lWeightInitValue: Any
    inb: Any
    im: Any
    logInb: Any
    iWeightInitValue: Any
    logBias: Any
    logSizeUp: Any
    chooserConfWidth: Any
    updateThresholdWidth: Any
    pUpdateThresholdWidth: Any
    extraWeightsWidth: Any
    scCountersWidth: Any
    initialUpdateThresholdValue: Any
    speculativeHistUpdate: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MPP_TAGE(TAGEBase):
    tunedHistoryLengths: Any
    numThreads: Any
    instShiftAmt: Any
    nHistoryTables: Any
    minHist: Any
    maxHist: Any
    tagTableTagWidths: Any
    logTagTableSizes: Any
    logRatioBiModalHystEntries: Any
    tagTableCounterBits: Any
    tagTableUBits: Any
    histBufferSize: Any
    pathHistBits: Any
    logUResetPeriod: Any
    numUseAltOnNa: Any
    initialTCounterValue: Any
    useAltOnNaBits: Any
    maxNumAlloc: Any
    noSkip: Any
    speculativeHistUpdate: Any
    takenOnlyHistory: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MPP_TAGE_8KB(MPP_TAGE):
    tunedHistoryLengths: Any
    numThreads: Any
    instShiftAmt: Any
    nHistoryTables: Any
    minHist: Any
    maxHist: Any
    tagTableTagWidths: Any
    logTagTableSizes: Any
    logRatioBiModalHystEntries: Any
    tagTableCounterBits: Any
    tagTableUBits: Any
    histBufferSize: Any
    pathHistBits: Any
    logUResetPeriod: Any
    numUseAltOnNa: Any
    initialTCounterValue: Any
    useAltOnNaBits: Any
    maxNumAlloc: Any
    noSkip: Any
    speculativeHistUpdate: Any
    takenOnlyHistory: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MRURP(BaseReplacementPolicy):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MasterPort(Port):

    def __init__(self, *args, **kwargs) -> None: ...


class MathExprPowerModel(PowerModelState):
    dyn: Any
    st: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Matrix_Unit(FUDesc):
    count: Any
    opList: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MaxCapacityPartitioningPolicy(BasePartitioningPolicy):
    cache_size: Any
    blk_size: Any
    partition_ids: Any
    capacities: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MemChecker(SimObject):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MemCheckerMonitor(SimObject):
    warn_only: Any
    memchecker: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MemCtrl(QoSMemCtrl):
    dram: Any
    write_high_thresh_perc: Any
    write_low_thresh_perc: Any
    min_writes_per_switch: Any
    min_reads_per_switch: Any
    mem_sched_policy: Any
    static_frontend_latency: Any
    static_backend_latency: Any
    command_window: Any
    disable_sanity_check: Any
    system: Any
    qos_priorities: Any
    qos_policy: Any
    qos_turnaround_policy: Any
    qos_q_policy: Any
    qos_syncro_scheduler: Any
    qos_priority_escalation: Any
    qos_requestors: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MemDelay(ClockedObject):
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MemFootprintProbe(BaseMemProbe):
    system: Any
    page_size: Any
    manager: Any
    probe_name: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MemInterface(AbstractMemory):
    write_buffer_size: Any
    read_buffer_size: Any
    addr_mapping: Any
    device_size: Any
    device_bus_width: Any
    burst_length: Any
    device_rowbuffer_size: Any
    devices_per_rank: Any
    ranks_per_channel: Any
    banks_per_rank: Any
    tCK: Any
    tBURST: Any
    tWTR: Any
    tRTW: Any
    tCS: Any
    range: Any
    null: Any
    in_addr_map: Any
    kvm_map: Any
    conf_table_reported: Any
    image_file: Any
    writeable: Any
    collect_stats: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MemSched(Enum):

    def __init__(self, *args, **kwargs) -> None: ...


class MemTest(ClockedObject):
    interval: Any
    size: Any
    base_addr_1: Any
    base_addr_2: Any
    uncacheable_base_addr: Any
    max_loads: Any
    percent_reads: Any
    percent_functional: Any
    percent_uncacheable: Any
    percent_atomic: Any
    progress_interval: Any
    progress_check: Any
    system: Any
    suppress_func_errors: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MemTraceProbe(BaseMemProbe):
    trace_compress: Any
    with_pc: Any
    trace_file: Any
    system: Any
    manager: Any
    probe_name: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MemoryBandwidth(float, ParamValue):

    def __init__(self, *args, **kwargs) -> None: ...


class MemoryMode(Enum):

    def __init__(self, *args, **kwargs) -> None: ...


class MemorySize(CheckedInt):

    def __init__(self, *args, **kwargs) -> None: ...


class MemorySize32(CheckedInt):

    def __init__(self, *args, **kwargs) -> None: ...


class MessageBuffer(SimObject):
    ordered: Any
    buffer_size: Any
    randomization: Any
    allow_zero_latency: Any
    max_dequeue_rate: Any
    routing_priority: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MessageRandomization(ScopedEnum):

    def __init__(self, *args, **kwargs) -> None: ...


class MinorDefaultFUPool(MinorFUPool):
    funcUnits: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MinorDefaultFloatSimdFU(MinorFU):
    opClasses: Any
    opLat: Any
    issueLat: Any
    timings: Any
    cantForwardFromFUIndices: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MinorDefaultIntDivFU(MinorFU):
    opClasses: Any
    opLat: Any
    issueLat: Any
    timings: Any
    cantForwardFromFUIndices: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MinorDefaultIntFU(MinorFU):
    opClasses: Any
    opLat: Any
    issueLat: Any
    timings: Any
    cantForwardFromFUIndices: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MinorDefaultIntMulFU(MinorFU):
    opClasses: Any
    opLat: Any
    issueLat: Any
    timings: Any
    cantForwardFromFUIndices: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MinorDefaultMemFU(MinorFU):
    opClasses: Any
    opLat: Any
    issueLat: Any
    timings: Any
    cantForwardFromFUIndices: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MinorDefaultMiscFU(MinorFU):
    opClasses: Any
    opLat: Any
    issueLat: Any
    timings: Any
    cantForwardFromFUIndices: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MinorDefaultPredFU(MinorFU):
    opClasses: Any
    opLat: Any
    issueLat: Any
    timings: Any
    cantForwardFromFUIndices: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MinorFU(SimObject):
    opClasses: Any
    opLat: Any
    issueLat: Any
    timings: Any
    cantForwardFromFUIndices: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MinorFUPool(SimObject):
    funcUnits: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MinorFUTiming(SimObject):
    mask: Any
    match: Any
    suppress: Any
    extraCommitLat: Any
    extraCommitLatExpr: Any
    extraAssumedLat: Any
    srcRegsRelativeLats: Any
    opClasses: Any
    description: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MinorOpClass(SimObject):
    opClass: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MinorOpClassSet(SimObject):
    opClasses: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MultiCompressor(BaseCacheCompressor):
    compressors: Any
    encoding_in_tags: Any
    block_size: Any
    chunk_size_bits: Any
    size_threshold_percentage: Any
    comp_chunks_per_cycle: Any
    comp_extra_latency: Any
    decomp_chunks_per_cycle: Any
    decomp_extra_latency: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MultiPrefetcher(BasePrefetcher):
    prefetchers: Any
    sys: Any
    block_size: Any
    on_miss: Any
    on_read: Any
    on_write: Any
    on_data: Any
    on_inst: Any
    prefetch_on_access: Any
    prefetch_on_pf_hit: Any
    use_virtual_addresses: Any
    page_bytes: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MultiperspectivePerceptron(ConditionalPredictor):
    num_filter_entries: Any
    num_local_histories: Any
    local_history_length: Any
    block_size: Any
    pcshift: Any
    threshold: Any
    bias0: Any
    bias1: Any
    biasmostly0: Any
    biasmostly1: Any
    nbest: Any
    tunebits: Any
    hshift: Any
    imli_mask1: Any
    imli_mask4: Any
    recencypos_mask: Any
    fudge: Any
    n_sign_bits: Any
    pcbit: Any
    decay: Any
    record_mask: Any
    hash_taken: Any
    tuneonly: Any
    extra_rounds: Any
    speed: Any
    initial_theta: Any
    budgetbits: Any
    speculative_update: Any
    initial_ghist_length: Any
    ignore_path_size: Any
    numThreads: Any
    instShiftAmt: Any
    speculativeHistUpdate: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MultiperspectivePerceptron64KB(MultiperspectivePerceptron):
    num_filter_entries: Any
    num_local_histories: Any
    local_history_length: Any
    block_size: Any
    pcshift: Any
    threshold: Any
    bias0: Any
    bias1: Any
    biasmostly0: Any
    biasmostly1: Any
    nbest: Any
    tunebits: Any
    hshift: Any
    imli_mask1: Any
    imli_mask4: Any
    recencypos_mask: Any
    fudge: Any
    n_sign_bits: Any
    pcbit: Any
    decay: Any
    record_mask: Any
    hash_taken: Any
    tuneonly: Any
    extra_rounds: Any
    speed: Any
    initial_theta: Any
    budgetbits: Any
    speculative_update: Any
    initial_ghist_length: Any
    ignore_path_size: Any
    numThreads: Any
    instShiftAmt: Any
    speculativeHistUpdate: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MultiperspectivePerceptron8KB(MultiperspectivePerceptron):
    num_filter_entries: Any
    num_local_histories: Any
    local_history_length: Any
    block_size: Any
    pcshift: Any
    threshold: Any
    bias0: Any
    bias1: Any
    biasmostly0: Any
    biasmostly1: Any
    nbest: Any
    tunebits: Any
    hshift: Any
    imli_mask1: Any
    imli_mask4: Any
    recencypos_mask: Any
    fudge: Any
    n_sign_bits: Any
    pcbit: Any
    decay: Any
    record_mask: Any
    hash_taken: Any
    tuneonly: Any
    extra_rounds: Any
    speed: Any
    initial_theta: Any
    budgetbits: Any
    speculative_update: Any
    initial_ghist_length: Any
    ignore_path_size: Any
    numThreads: Any
    instShiftAmt: Any
    speculativeHistUpdate: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MultiperspectivePerceptronTAGE(MultiperspectivePerceptron):
    tage: Any
    loop_predictor: Any
    statistical_corrector: Any
    num_filter_entries: Any
    num_local_histories: Any
    local_history_length: Any
    block_size: Any
    pcshift: Any
    threshold: Any
    bias0: Any
    bias1: Any
    biasmostly0: Any
    biasmostly1: Any
    nbest: Any
    tunebits: Any
    hshift: Any
    imli_mask1: Any
    imli_mask4: Any
    recencypos_mask: Any
    fudge: Any
    n_sign_bits: Any
    pcbit: Any
    decay: Any
    record_mask: Any
    hash_taken: Any
    tuneonly: Any
    extra_rounds: Any
    speed: Any
    initial_theta: Any
    budgetbits: Any
    speculative_update: Any
    initial_ghist_length: Any
    ignore_path_size: Any
    numThreads: Any
    instShiftAmt: Any
    speculativeHistUpdate: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MultiperspectivePerceptronTAGE64KB(MultiperspectivePerceptronTAGE):
    tage: Any
    loop_predictor: Any
    statistical_corrector: Any
    num_filter_entries: Any
    num_local_histories: Any
    local_history_length: Any
    block_size: Any
    pcshift: Any
    threshold: Any
    bias0: Any
    bias1: Any
    biasmostly0: Any
    biasmostly1: Any
    nbest: Any
    tunebits: Any
    hshift: Any
    imli_mask1: Any
    imli_mask4: Any
    recencypos_mask: Any
    fudge: Any
    n_sign_bits: Any
    pcbit: Any
    decay: Any
    record_mask: Any
    hash_taken: Any
    tuneonly: Any
    extra_rounds: Any
    speed: Any
    initial_theta: Any
    budgetbits: Any
    speculative_update: Any
    initial_ghist_length: Any
    ignore_path_size: Any
    numThreads: Any
    instShiftAmt: Any
    speculativeHistUpdate: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class MultiperspectivePerceptronTAGE8KB(MultiperspectivePerceptronTAGE):
    tage: Any
    loop_predictor: Any
    statistical_corrector: Any
    num_filter_entries: Any
    num_local_histories: Any
    local_history_length: Any
    block_size: Any
    pcshift: Any
    threshold: Any
    bias0: Any
    bias1: Any
    biasmostly0: Any
    biasmostly1: Any
    nbest: Any
    tunebits: Any
    hshift: Any
    imli_mask1: Any
    imli_mask4: Any
    recencypos_mask: Any
    fudge: Any
    n_sign_bits: Any
    pcbit: Any
    decay: Any
    record_mask: Any
    hash_taken: Any
    tuneonly: Any
    extra_rounds: Any
    speed: Any
    initial_theta: Any
    budgetbits: Any
    speculative_update: Any
    initial_ghist_length: Any
    ignore_path_size: Any
    numThreads: Any
    instShiftAmt: Any
    speculativeHistUpdate: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class NRURP(BRRIPRP):
    num_bits: Any
    hit_priority: Any
    btp: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class NSGigE(EtherDevBase):
    dma_data_free: Any
    dma_desc_free: Any
    dma_no_allocate: Any
    hardware_address: Any
    dma_read_delay: Any
    dma_read_factor: Any
    dma_write_delay: Any
    dma_write_factor: Any
    rx_delay: Any
    tx_delay: Any
    rx_fifo_size: Any
    tx_fifo_size: Any
    rx_filter: Any
    intr_delay: Any
    rx_thread: Any
    tx_thread: Any
    rss: Any
    BAR0: Any
    BAR1: Any
    BAR2: Any
    BAR3: Any
    BAR4: Any
    BAR5: Any
    CardbusCIS: Any
    SubsystemID: Any
    SubsystemVendorID: Any
    ExpansionROM: Any
    MaximumLatency: Any
    MinimumGrant: Any
    upstream: Any
    pci_dev: Any
    pci_func: Any
    pio_latency: Any
    config_latency: Any
    VendorID: Any
    DeviceID: Any
    Command: Any
    Status: Any
    Revision: Any
    ProgIF: Any
    SubClassCode: Any
    ClassCode: Any
    CacheLineSize: Any
    LatencyTimer: Any
    HeaderType: Any
    BIST: Any
    CapabilityPtr: Any
    InterruptLine: Any
    InterruptPin: Any
    PMCAPBaseOffset: Any
    PMCAPNextCapability: Any
    PMCAPCapId: Any
    PMCAPCapabilities: Any
    PMCAPCtrlStatus: Any
    MSICAPBaseOffset: Any
    MSICAPNextCapability: Any
    MSICAPCapId: Any
    MSICAPMsgCtrl: Any
    MSICAPMsgAddr: Any
    MSICAPMsgUpperAddr: Any
    MSICAPMsgData: Any
    MSICAPMaskBits: Any
    MSICAPPendingBits: Any
    MSIXCAPBaseOffset: Any
    MSIXCAPNextCapability: Any
    MSIXCAPCapId: Any
    MSIXMsgCtrl: Any
    MSIXTableOffset: Any
    MSIXPbaOffset: Any
    PXCAPBaseOffset: Any
    PXCAPNextCapability: Any
    PXCAPCapId: Any
    PXCAPCapabilities: Any
    PXCAPDevCapabilities: Any
    PXCAPDevCtrl: Any
    PXCAPDevStatus: Any
    PXCAPLinkCap: Any
    PXCAPLinkCtrl: Any
    PXCAPLinkStatus: Any
    PXCAPSlotCap: Any
    PXCAPSlotCtrl: Any
    PXCAPSlotStatus: Any
    PXCAPRootCap: Any
    PXCAPRootCtrl: Any
    PXCAPRootStatus: Any
    PXCAPDevCap2: Any
    PXCAPDevCtrl2: Any
    PXCAPDevStatus2: Any
    PXCAPLinkCap2: Any
    PXCAPLinkCtrl2: Any
    PXCAPLinkStatus2: Any
    PXCAPSlotCap2: Any
    PXCAPSlotCtrl2: Any
    PXCAPSlotStatus2: Any
    sid: Any
    ssid: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class NVMInterface(MemInterface):
    max_pending_writes: Any
    max_pending_reads: Any
    tREAD: Any
    tWRITE: Any
    tSEND: Any
    two_cycle_rdwr: Any
    write_buffer_size: Any
    read_buffer_size: Any
    addr_mapping: Any
    device_size: Any
    device_bus_width: Any
    burst_length: Any
    device_rowbuffer_size: Any
    devices_per_rank: Any
    ranks_per_channel: Any
    banks_per_rank: Any
    tCK: Any
    tBURST: Any
    tWTR: Any
    tRTW: Any
    tCS: Any
    range: Any
    null: Any
    in_addr_map: Any
    kvm_map: Any
    conf_table_reported: Any
    image_file: Any
    writeable: Any
    collect_stats: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class NVM_2400_1x64(NVMInterface):
    max_pending_writes: Any
    max_pending_reads: Any
    tREAD: Any
    tWRITE: Any
    tSEND: Any
    two_cycle_rdwr: Any
    write_buffer_size: Any
    read_buffer_size: Any
    addr_mapping: Any
    device_size: Any
    device_bus_width: Any
    burst_length: Any
    device_rowbuffer_size: Any
    devices_per_rank: Any
    ranks_per_channel: Any
    banks_per_rank: Any
    tCK: Any
    tBURST: Any
    tWTR: Any
    tRTW: Any
    tCS: Any
    range: Any
    null: Any
    in_addr_map: Any
    kvm_map: Any
    conf_table_reported: Any
    image_file: Any
    writeable: Any
    collect_stats: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class NativeTrace(ExeTracer):
    disassembler: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class NetworkBandwidth(float, ParamValue):

    def __init__(self, *args, **kwargs) -> None: ...


class NetworkBridge(CreditLink):
    link: Any
    vtype: Any
    serdes_latency: Any
    cdc_latency: Any
    link_id: Any
    link_latency: Any
    vcs_per_vnet: Any
    virt_nets: Any
    supported_vnets: Any
    width: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class NetworkLink(ClockedObject):
    link_id: Any
    link_latency: Any
    vcs_per_vnet: Any
    virt_nets: Any
    supported_vnets: Any
    width: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class NonCachingSimpleCPU(BaseNonCachingSimpleCPU, X86CPU):
    width: Any
    simulate_data_stalls: Any
    simulate_inst_stalls: Any
    branchPred: Any
    system: Any
    cpu_id: Any
    socket_id: Any
    numThreads: Any
    pwr_gating_latency: Any
    power_gating_on_idle: Any
    function_trace: Any
    function_trace_start: Any
    checker: Any
    syscallRetryLatency: Any
    do_checkpoint_insts: Any
    do_statistics_insts: Any
    workload: Any
    mmu: Any
    interrupts: Any
    isa: Any
    decoder: Any
    max_insts_all_threads: Any
    max_insts_any_thread: Any
    simpoint_start_insts: Any
    progress_interval: Any
    switched_out: Any
    tracer: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class NoncoherentCache(BaseCache):
    size: Any
    assoc: Any
    tag_latency: Any
    data_latency: Any
    response_latency: Any
    warmup_percentage: Any
    max_miss_count: Any
    mshrs: Any
    demand_mshr_reserve: Any
    tgts_per_mshr: Any
    write_buffers: Any
    is_read_only: Any
    prefetcher: Any
    tags: Any
    replacement_policy: Any
    partitioning_manager: Any
    compressor: Any
    replace_expansions: Any
    move_contractions: Any
    sequential_access: Any
    addr_ranges: Any
    system: Any
    writeback_clean: Any
    clusivity: Any
    write_allocator: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class NoncoherentXBar(BaseXBar):
    frontend_latency: Any
    forward_latency: Any
    response_latency: Any
    header_latency: Any
    width: Any
    use_default_range: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class O3CPU(BaseO3CPU, X86CPU):
    activity: Any
    cacheStorePorts: Any
    cacheLoadPorts: Any
    fetchToBacDelay: Any
    decodeToFetchDelay: Any
    renameToFetchDelay: Any
    iewToFetchDelay: Any
    commitToFetchDelay: Any
    fetchWidth: Any
    fetchBufferSize: Any
    fetchQueueSize: Any
    renameToDecodeDelay: Any
    iewToDecodeDelay: Any
    commitToDecodeDelay: Any
    bacToFetchDelay: Any
    fetchToDecodeDelay: Any
    decodeWidth: Any
    iewToRenameDelay: Any
    commitToRenameDelay: Any
    decodeToRenameDelay: Any
    renameWidth: Any
    commitToIEWDelay: Any
    renameToIEWDelay: Any
    issueToExecuteDelay: Any
    dispatchWidth: Any
    issueWidth: Any
    wbWidth: Any
    iewToCommitDelay: Any
    renameToROBDelay: Any
    commitWidth: Any
    squashWidth: Any
    trapLatency: Any
    fetchTrapLatency: Any
    backComSize: Any
    forwardComSize: Any
    LQEntries: Any
    SQEntries: Any
    LSQDepCheckShift: Any
    LSQCheckLoads: Any
    store_set_clear_period: Any
    LFSTSize: Any
    SSITSize: Any
    SSITAssoc: Any
    SSITReplPolicy: Any
    SSITIndexingPolicy: Any
    numRobs: Any
    numPhysIntRegs: Any
    numPhysFloatRegs: Any
    numPhysVecRegs: Any
    numPhysVecPredRegs: Any
    numPhysMatRegs: Any
    numPhysCCRegs: Any
    instQueues: Any
    numROBEntries: Any
    smtNumFetchingThreads: Any
    smtFetchPolicy: Any
    smtLSQPolicy: Any
    smtLSQThreshold: Any
    smtROBPolicy: Any
    smtROBThreshold: Any
    smtCommitPolicy: Any
    branchPred: Any
    needsTSO: Any
    recvRespThrottling: Any
    recvRespMaxCachelines: Any
    recvRespBufferSize: Any
    decoupledFrontEnd: Any
    numFTQEntries: Any
    minInstSize: Any
    fetchTargetWidth: Any
    maxFTPerCycle: Any
    maxTakenPredPerCycle: Any
    system: Any
    cpu_id: Any
    socket_id: Any
    numThreads: Any
    pwr_gating_latency: Any
    power_gating_on_idle: Any
    function_trace: Any
    function_trace_start: Any
    checker: Any
    syscallRetryLatency: Any
    do_checkpoint_insts: Any
    do_statistics_insts: Any
    workload: Any
    mmu: Any
    interrupts: Any
    isa: Any
    decoder: Any
    max_insts_all_threads: Any
    max_insts_any_thread: Any
    simpoint_start_insts: Any
    progress_interval: Any
    switched_out: Any
    tracer: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class OpClass(Enum):

    def __init__(self, *args, **kwargs) -> None: ...


class OpDesc(SimObject):
    opClass: Any
    opLat: Any
    pipelined: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class OptionalParamDesc(SingleTypeParamDesc):

    def __init__(self, *args, **kwargs) -> None: ...


class OutgoingRequestBridge(SimObject):
    physical_address_ranges: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class PIFPrefetcher(QueuedPrefetcher):
    prec_spatial_region_bits: Any
    succ_spatial_region_bits: Any
    compactor_entries: Any
    stream_address_buffer_entries: Any
    history_buffer_size: Any
    index_entries: Any
    index_assoc: Any
    index_indexing_policy: Any
    index_replacement_policy: Any
    latency: Any
    queue_size: Any
    max_prefetch_requests_with_pending_translation: Any
    queue_squash: Any
    queue_filter: Any
    cache_snoop: Any
    tag_prefetch: Any
    throttle_control_percentage: Any
    sys: Any
    block_size: Any
    on_miss: Any
    on_read: Any
    on_write: Any
    on_data: Any
    on_inst: Any
    prefetch_on_access: Any
    prefetch_on_pf_hit: Any
    use_virtual_addresses: Any
    page_bytes: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class PMType(Enum):

    def __init__(self, *args, **kwargs) -> None: ...


class PS2Device(SimObject):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class PS2Keyboard(PS2Device):
    vnc: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class PS2Mouse(PS2Device):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class PS2TouchKit(PS2Device):
    vnc: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class PageManage(Enum):

    def __init__(self, *args, **kwargs) -> None: ...


class ParamDesc:

    def __init__(self, *args, **kwargs) -> None: ...


class ParamValue:

    def __init__(self, *args, **kwargs) -> None: ...


class PartitionManager(SimObject):
    partitioning_policies: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Pc(Platform):
    system: Any
    south_bridge: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class PcCountPair(ParamValue):

    def __init__(self, *args, **kwargs) -> None: ...


class PcCountTracker(ProbeListenerObject):
    targets: Any
    core: Any
    ptmanager: Any
    manager: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class PcCountTrackerManager(SimObject):
    targets: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class PcPciHost(GenericPciHost):
    platform: Any
    conf_base: Any
    conf_size: Any
    conf_device_bits: Any
    pci_pio_base: Any
    pci_mem_base: Any
    pci_dma_base: Any
    up_to_down: Any
    down_to_up: Any
    config_error: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class PcSpeaker(BasicPioDevice):
    i8254: Any
    pio_addr: Any
    pio_latency: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class PciBar(SimObject):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class PciBarNone(PciBar):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class PciBus(NoncoherentXBar):
    frontend_latency: Any
    forward_latency: Any
    response_latency: Any
    header_latency: Any
    width: Any
    use_default_range: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class PciConfigError(IsaFake):
    pio_addr: Any
    pio_size: Any
    ret_data8: Any
    ret_data16: Any
    ret_data32: Any
    ret_data64: Any
    ret_bad_addr: Any
    update_data: Any
    warn_access: Any
    fake_mem: Any
    pio_latency: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class PciDevice(DmaDevice):
    upstream: Any
    pci_dev: Any
    pci_func: Any
    pio_latency: Any
    config_latency: Any
    VendorID: Any
    DeviceID: Any
    Command: Any
    Status: Any
    Revision: Any
    ProgIF: Any
    SubClassCode: Any
    ClassCode: Any
    CacheLineSize: Any
    LatencyTimer: Any
    HeaderType: Any
    BIST: Any
    CapabilityPtr: Any
    InterruptLine: Any
    InterruptPin: Any
    PMCAPBaseOffset: Any
    PMCAPNextCapability: Any
    PMCAPCapId: Any
    PMCAPCapabilities: Any
    PMCAPCtrlStatus: Any
    MSICAPBaseOffset: Any
    MSICAPNextCapability: Any
    MSICAPCapId: Any
    MSICAPMsgCtrl: Any
    MSICAPMsgAddr: Any
    MSICAPMsgUpperAddr: Any
    MSICAPMsgData: Any
    MSICAPMaskBits: Any
    MSICAPPendingBits: Any
    MSIXCAPBaseOffset: Any
    MSIXCAPNextCapability: Any
    MSIXCAPCapId: Any
    MSIXMsgCtrl: Any
    MSIXTableOffset: Any
    MSIXPbaOffset: Any
    PXCAPBaseOffset: Any
    PXCAPNextCapability: Any
    PXCAPCapId: Any
    PXCAPCapabilities: Any
    PXCAPDevCapabilities: Any
    PXCAPDevCtrl: Any
    PXCAPDevStatus: Any
    PXCAPLinkCap: Any
    PXCAPLinkCtrl: Any
    PXCAPLinkStatus: Any
    PXCAPSlotCap: Any
    PXCAPSlotCtrl: Any
    PXCAPSlotStatus: Any
    PXCAPRootCap: Any
    PXCAPRootCtrl: Any
    PXCAPRootStatus: Any
    PXCAPDevCap2: Any
    PXCAPDevCtrl2: Any
    PXCAPDevStatus2: Any
    PXCAPLinkCap2: Any
    PXCAPLinkCtrl2: Any
    PXCAPLinkStatus2: Any
    PXCAPSlotCap2: Any
    PXCAPSlotCtrl2: Any
    PXCAPSlotStatus2: Any
    sid: Any
    ssid: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class PciEndpoint(PciDevice):
    BAR0: Any
    BAR1: Any
    BAR2: Any
    BAR3: Any
    BAR4: Any
    BAR5: Any
    CardbusCIS: Any
    SubsystemID: Any
    SubsystemVendorID: Any
    ExpansionROM: Any
    MaximumLatency: Any
    MinimumGrant: Any
    upstream: Any
    pci_dev: Any
    pci_func: Any
    pio_latency: Any
    config_latency: Any
    VendorID: Any
    DeviceID: Any
    Command: Any
    Status: Any
    Revision: Any
    ProgIF: Any
    SubClassCode: Any
    ClassCode: Any
    CacheLineSize: Any
    LatencyTimer: Any
    HeaderType: Any
    BIST: Any
    CapabilityPtr: Any
    InterruptLine: Any
    InterruptPin: Any
    PMCAPBaseOffset: Any
    PMCAPNextCapability: Any
    PMCAPCapId: Any
    PMCAPCapabilities: Any
    PMCAPCtrlStatus: Any
    MSICAPBaseOffset: Any
    MSICAPNextCapability: Any
    MSICAPCapId: Any
    MSICAPMsgCtrl: Any
    MSICAPMsgAddr: Any
    MSICAPMsgUpperAddr: Any
    MSICAPMsgData: Any
    MSICAPMaskBits: Any
    MSICAPPendingBits: Any
    MSIXCAPBaseOffset: Any
    MSIXCAPNextCapability: Any
    MSIXCAPCapId: Any
    MSIXMsgCtrl: Any
    MSIXTableOffset: Any
    MSIXPbaOffset: Any
    PXCAPBaseOffset: Any
    PXCAPNextCapability: Any
    PXCAPCapId: Any
    PXCAPCapabilities: Any
    PXCAPDevCapabilities: Any
    PXCAPDevCtrl: Any
    PXCAPDevStatus: Any
    PXCAPLinkCap: Any
    PXCAPLinkCtrl: Any
    PXCAPLinkStatus: Any
    PXCAPSlotCap: Any
    PXCAPSlotCtrl: Any
    PXCAPSlotStatus: Any
    PXCAPRootCap: Any
    PXCAPRootCtrl: Any
    PXCAPRootStatus: Any
    PXCAPDevCap2: Any
    PXCAPDevCtrl2: Any
    PXCAPDevStatus2: Any
    PXCAPLinkCap2: Any
    PXCAPLinkCtrl2: Any
    PXCAPLinkStatus2: Any
    PXCAPSlotCap2: Any
    PXCAPSlotCtrl2: Any
    PXCAPSlotStatus2: Any
    sid: Any
    ssid: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class PciHost(PciUpstream):
    up_to_down: Any
    down_to_up: Any
    config_error: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class PciIoBar(PciBar):
    size: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class PciLegacyIoBar(PciIoBar):
    addr: Any
    size: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class PciMemBar(PciBar):
    size: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class PciMemUpperBar(PciBar):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class PciType1Device(PciDevice):
    BAR0: Any
    BAR1: Any
    PrimaryBusNumber: Any
    SecondaryBusNumber: Any
    SubordinateBusNumber: Any
    SecondaryLatencyTimer: Any
    IOBase: Any
    IOLimit: Any
    SecondaryStatus: Any
    MemoryBase: Any
    MemoryLimit: Any
    PrefetchableMemoryBase: Any
    PrefetchableMemoryLimit: Any
    PrefetchableBaseUpper: Any
    PrefetchableLimitUpper: Any
    IOBaseUpper: Any
    IOLimitUpper: Any
    ExpansionROM: Any
    BridgeControl: Any
    upstream: Any
    pci_dev: Any
    pci_func: Any
    pio_latency: Any
    config_latency: Any
    VendorID: Any
    DeviceID: Any
    Command: Any
    Status: Any
    Revision: Any
    ProgIF: Any
    SubClassCode: Any
    ClassCode: Any
    CacheLineSize: Any
    LatencyTimer: Any
    HeaderType: Any
    BIST: Any
    CapabilityPtr: Any
    InterruptLine: Any
    InterruptPin: Any
    PMCAPBaseOffset: Any
    PMCAPNextCapability: Any
    PMCAPCapId: Any
    PMCAPCapabilities: Any
    PMCAPCtrlStatus: Any
    MSICAPBaseOffset: Any
    MSICAPNextCapability: Any
    MSICAPCapId: Any
    MSICAPMsgCtrl: Any
    MSICAPMsgAddr: Any
    MSICAPMsgUpperAddr: Any
    MSICAPMsgData: Any
    MSICAPMaskBits: Any
    MSICAPPendingBits: Any
    MSIXCAPBaseOffset: Any
    MSIXCAPNextCapability: Any
    MSIXCAPCapId: Any
    MSIXMsgCtrl: Any
    MSIXTableOffset: Any
    MSIXPbaOffset: Any
    PXCAPBaseOffset: Any
    PXCAPNextCapability: Any
    PXCAPCapId: Any
    PXCAPCapabilities: Any
    PXCAPDevCapabilities: Any
    PXCAPDevCtrl: Any
    PXCAPDevStatus: Any
    PXCAPLinkCap: Any
    PXCAPLinkCtrl: Any
    PXCAPLinkStatus: Any
    PXCAPSlotCap: Any
    PXCAPSlotCtrl: Any
    PXCAPSlotStatus: Any
    PXCAPRootCap: Any
    PXCAPRootCtrl: Any
    PXCAPRootStatus: Any
    PXCAPDevCap2: Any
    PXCAPDevCtrl2: Any
    PXCAPDevStatus2: Any
    PXCAPLinkCap2: Any
    PXCAPLinkCtrl2: Any
    PXCAPLinkStatus2: Any
    PXCAPSlotCap2: Any
    PXCAPSlotCtrl2: Any
    PXCAPSlotStatus2: Any
    sid: Any
    ssid: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class PciUpDownBridge(BridgeBase):
    req_size: Any
    resp_size: Any
    delay: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class PciUpstream(ClockedObject):
    up_to_down: Any
    down_to_up: Any
    config_error: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class PciVirtIO(PciEndpoint):
    vio: Any
    BAR0: Any
    BAR1: Any
    BAR2: Any
    BAR3: Any
    BAR4: Any
    BAR5: Any
    CardbusCIS: Any
    SubsystemID: Any
    SubsystemVendorID: Any
    ExpansionROM: Any
    MaximumLatency: Any
    MinimumGrant: Any
    upstream: Any
    pci_dev: Any
    pci_func: Any
    pio_latency: Any
    config_latency: Any
    VendorID: Any
    DeviceID: Any
    Command: Any
    Status: Any
    Revision: Any
    ProgIF: Any
    SubClassCode: Any
    ClassCode: Any
    CacheLineSize: Any
    LatencyTimer: Any
    HeaderType: Any
    BIST: Any
    CapabilityPtr: Any
    InterruptLine: Any
    InterruptPin: Any
    PMCAPBaseOffset: Any
    PMCAPNextCapability: Any
    PMCAPCapId: Any
    PMCAPCapabilities: Any
    PMCAPCtrlStatus: Any
    MSICAPBaseOffset: Any
    MSICAPNextCapability: Any
    MSICAPCapId: Any
    MSICAPMsgCtrl: Any
    MSICAPMsgAddr: Any
    MSICAPMsgUpperAddr: Any
    MSICAPMsgData: Any
    MSICAPMaskBits: Any
    MSICAPPendingBits: Any
    MSIXCAPBaseOffset: Any
    MSIXCAPNextCapability: Any
    MSIXCAPCapId: Any
    MSIXMsgCtrl: Any
    MSIXTableOffset: Any
    MSIXPbaOffset: Any
    PXCAPBaseOffset: Any
    PXCAPNextCapability: Any
    PXCAPCapId: Any
    PXCAPCapabilities: Any
    PXCAPDevCapabilities: Any
    PXCAPDevCtrl: Any
    PXCAPDevStatus: Any
    PXCAPLinkCap: Any
    PXCAPLinkCtrl: Any
    PXCAPLinkStatus: Any
    PXCAPSlotCap: Any
    PXCAPSlotCtrl: Any
    PXCAPSlotStatus: Any
    PXCAPRootCap: Any
    PXCAPRootCtrl: Any
    PXCAPRootStatus: Any
    PXCAPDevCap2: Any
    PXCAPDevCtrl2: Any
    PXCAPDevStatus2: Any
    PXCAPLinkCap2: Any
    PXCAPLinkCtrl2: Any
    PXCAPLinkStatus2: Any
    PXCAPSlotCap2: Any
    PXCAPSlotCtrl2: Any
    PXCAPSlotStatus2: Any
    sid: Any
    ssid: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Percent(CheckedInt):

    def __init__(self, *args, **kwargs) -> None: ...


class PerfectCompressor(BaseCacheCompressor):
    max_compression_ratio: Any
    block_size: Any
    chunk_size_bits: Any
    size_threshold_percentage: Any
    comp_chunks_per_cycle: Any
    comp_extra_latency: Any
    decomp_chunks_per_cycle: Any
    decomp_extra_latency: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class PioDevice(ClockedObject):
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Platform(SimObject):
    system: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Port:

    def __init__(self, *args, **kwargs) -> None: ...


class PortTerminator(SimObject):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class PowerDomain(PowerState):
    default_state: Any
    possible_states: Any
    clk_gate_min: Any
    clk_gate_max: Any
    clk_gate_bins: Any
    leaders: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class PowerModel(SimObject):
    pm: Any
    subsystem: Any
    pm_type: Any
    ambient_temp: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class PowerModelState(SimObject):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class PowerState(SimObject):
    default_state: Any
    possible_states: Any
    clk_gate_min: Any
    clk_gate_max: Any
    clk_gate_bins: Any
    leaders: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class PredALU(FUDesc):
    count: Any
    opList: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Prefetcher(RubyPrefetcher):
    num_streams: Any
    unit_filter: Any
    nonunit_filter: Any
    train_misses: Any
    num_startup_pfs: Any
    cross_page: Any
    page_shift: Any
    block_size: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class ProbeListenerObject(SimObject):
    manager: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Process(SimObject):
    input: Any
    output: Any
    errout: Any
    system: Any
    useArchPT: Any
    kvmInSE: Any
    maxStackSize: Any
    zeroPages: Any
    uid: Any
    euid: Any
    gid: Any
    egid: Any
    pid: Any
    ppid: Any
    pgid: Any
    executable: Any
    cmd: Any
    env: Any
    cwd: Any
    simpoint: Any
    drivers: Any
    release: Any
    architecture_strategy: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class PwrState(Enum):

    def __init__(self, *args, **kwargs) -> None: ...


class PyBindExport:

    def __init__(self, *args, **kwargs) -> None: ...


class PyBindMethod(PyBindExport):

    def __init__(self, *args, **kwargs) -> None: ...


class PyBindProperty(PyBindExport):

    def __init__(self, *args, **kwargs) -> None: ...


class PyTrafficGen(BaseTrafficGen):
    system: Any
    elastic_req: Any
    max_outstanding_reqs: Any
    progress_check: Any
    stream_gen: Any
    sids: Any
    ssids: Any
    cpu_id: Any
    socket_id: Any
    numThreads: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class QemuFwCfg(PioDevice):
    items: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class QemuFwCfgIo(QemuFwCfg):
    selector_addr: Any
    items: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class QemuFwCfgItem(SimObject):
    arch_specific: Any
    index: Any
    path: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class QemuFwCfgItemBytes(QemuFwCfgItem):
    data: Any
    arch_specific: Any
    index: Any
    path: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class QemuFwCfgItemE820(QemuFwCfgItem):
    entries: Any
    arch_specific: Any
    index: Any
    path: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class QemuFwCfgItemFile(QemuFwCfgItem):
    file: Any
    arch_specific: Any
    index: Any
    path: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class QemuFwCfgItemString(QemuFwCfgItem):
    string: Any
    arch_specific: Any
    index: Any
    path: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class QemuFwCfgMmio(QemuFwCfg):
    selector_addr: Any
    data_addr_range: Any
    items: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class QoSFixedPriorityPolicy(QoSPolicy):
    qos_fixed_prio_default_prio: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class QoSMemCtrl(ClockedObject):
    system: Any
    qos_priorities: Any
    qos_policy: Any
    qos_turnaround_policy: Any
    qos_q_policy: Any
    qos_syncro_scheduler: Any
    qos_priority_escalation: Any
    qos_requestors: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class QoSMemSinkCtrl(QoSMemCtrl):
    interface: Any
    write_buffer_size: Any
    read_buffer_size: Any
    memory_packet_size: Any
    request_latency: Any
    response_latency: Any
    system: Any
    qos_priorities: Any
    qos_policy: Any
    qos_turnaround_policy: Any
    qos_q_policy: Any
    qos_syncro_scheduler: Any
    qos_priority_escalation: Any
    qos_requestors: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class QoSMemSinkInterface(AbstractMemory):
    range: Any
    null: Any
    in_addr_map: Any
    kvm_map: Any
    conf_table_reported: Any
    image_file: Any
    writeable: Any
    collect_stats: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class QoSPolicy(SimObject):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class QoSPropFairPolicy(QoSPolicy):
    weight: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class QoSQPolicy(Enum):

    def __init__(self, *args, **kwargs) -> None: ...


class QoSTurnaroundPolicy(SimObject):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class QoSTurnaroundPolicyIdeal(QoSTurnaroundPolicy):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class QueuedPrefetcher(BasePrefetcher):
    latency: Any
    queue_size: Any
    max_prefetch_requests_with_pending_translation: Any
    queue_squash: Any
    queue_filter: Any
    cache_snoop: Any
    tag_prefetch: Any
    throttle_control_percentage: Any
    sys: Any
    block_size: Any
    on_miss: Any
    on_read: Any
    on_write: Any
    on_data: Any
    on_inst: Any
    prefetch_on_access: Any
    prefetch_on_pf_hit: Any
    use_virtual_addresses: Any
    page_bytes: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class RRIPRP(BRRIPRP):
    num_bits: Any
    hit_priority: Any
    btp: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class RandomRP(BaseReplacementPolicy):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class RangeAddrMapper(AddrMapper):
    original_ranges: Any
    remapped_ranges: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class RawDiskImage(DiskImage):
    image_file: Any
    read_only: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class RdWrPort(FUDesc):
    count: Any
    opList: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class ReadPort(FUDesc):
    count: Any
    opList: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class RedirectPath(SimObject):
    app_path: Any
    host_paths: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class RepeatedQwordsCompressor(BaseDictionaryCompressor):
    dictionary_size: Any
    block_size: Any
    chunk_size_bits: Any
    size_threshold_percentage: Any
    comp_chunks_per_cycle: Any
    comp_extra_latency: Any
    decomp_chunks_per_cycle: Any
    decomp_extra_latency: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class RequestPort(Port):

    def __init__(self, *args, **kwargs) -> None: ...


class ResetRequestPort(Port):

    def __init__(self, *args, **kwargs) -> None: ...


class ResetResponsePort(Port):

    def __init__(self, *args, **kwargs) -> None: ...


class ResponsePort(Port):

    def __init__(self, *args, **kwargs) -> None: ...


class ReturnAddrStack(SimObject):
    numThreads: Any
    numEntries: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class RiscvUart8250(Uart8250):
    pio_size: Any
    platform: Any
    device: Any
    pio_addr: Any
    pio_latency: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Root(SimObject):
    sim_quantum: Any
    full_system: Any
    time_sync_enable: Any
    time_sync_period: Any
    time_sync_spin_threshold: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class RubyCache(SimObject):
    size: Any
    assoc: Any
    replacement_policy: Any
    start_index_bit: Any
    is_icache: Any
    block_size: Any
    atomicLatency: Any
    atomicALUs: Any
    dataArrayBanks: Any
    tagArrayBanks: Any
    dataAccessLatency: Any
    tagAccessLatency: Any
    resourceStalls: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class RubyController(ClockedObject):
    version: Any
    addr_ranges: Any
    cluster_id: Any
    transitions_per_cycle: Any
    buffer_size: Any
    recycle_latency: Any
    number_of_TBEs: Any
    ruby_system: Any
    mandatory_queue_latency: Any
    system: Any
    upstream_destinations: Any
    downstream_destinations: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class RubyDirectedTester(ClockedObject):
    requests_to_complete: Any
    generator: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class RubyDirectoryMemory(SimObject):
    addr_ranges: Any
    block_size: Any
    ruby_system: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class RubyHTMSequencer(RubySequencer):
    dcache: Any
    max_outstanding_requests: Any
    deadlock_threshold: Any
    garnet_standalone: Any
    coreid: Any
    version: Any
    using_ruby_tester: Any
    no_retry_on_stall: Any
    ruby_system: Any
    system: Any
    support_data_reqs: Any
    support_inst_reqs: Any
    is_cpu_sequencer: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class RubyNetwork(ClockedObject):
    topology: Any
    number_of_virtual_networks: Any
    control_msg_size: Any
    ruby_system: Any
    routers: Any
    netifs: Any
    ext_links: Any
    int_links: Any
    data_msg_size: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class RubyPort(ClockedObject):
    version: Any
    using_ruby_tester: Any
    no_retry_on_stall: Any
    ruby_system: Any
    system: Any
    support_data_reqs: Any
    support_inst_reqs: Any
    is_cpu_sequencer: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class RubyPortProxy(RubyPort):
    version: Any
    using_ruby_tester: Any
    no_retry_on_stall: Any
    ruby_system: Any
    system: Any
    support_data_reqs: Any
    support_inst_reqs: Any
    is_cpu_sequencer: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class RubyPrefetcher(SimObject):
    num_streams: Any
    unit_filter: Any
    nonunit_filter: Any
    train_misses: Any
    num_startup_pfs: Any
    cross_page: Any
    page_shift: Any
    block_size: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class RubySequencer(RubyPort):
    dcache: Any
    max_outstanding_requests: Any
    deadlock_threshold: Any
    garnet_standalone: Any
    coreid: Any
    version: Any
    using_ruby_tester: Any
    no_retry_on_stall: Any
    ruby_system: Any
    system: Any
    support_data_reqs: Any
    support_inst_reqs: Any
    is_cpu_sequencer: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class RubySystem(ClockedObject):
    randomization: Any
    block_size_bytes: Any
    memory_size_bits: Any
    phys_mem: Any
    system: Any
    access_backing_store: Any
    hot_lines: Any
    all_instructions: Any
    num_of_sequencers: Any
    number_of_virtual_networks: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class RubyTester(ClockedObject):
    num_cpus: Any
    checks_to_complete: Any
    deadlock_threshold: Any
    wakeup_frequency: Any
    check_flush: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class RubyWireBuffer(SimObject):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SBOOEPrefetcher(QueuedPrefetcher):
    latency_buffer_size: Any
    sequential_prefetchers: Any
    sandbox_entries: Any
    score_threshold_pct: Any
    latency: Any
    queue_size: Any
    max_prefetch_requests_with_pending_translation: Any
    queue_squash: Any
    queue_filter: Any
    cache_snoop: Any
    tag_prefetch: Any
    throttle_control_percentage: Any
    sys: Any
    block_size: Any
    on_miss: Any
    on_read: Any
    on_write: Any
    on_data: Any
    on_inst: Any
    prefetch_on_access: Any
    prefetch_on_pf_hit: Any
    use_virtual_addresses: Any
    page_bytes: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SEWorkload(Workload):
    wait_for_remote_gdb: Any
    remote_gdb_port: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SEWorkloadMeta(MetaSimObject):

    def __init__(self, *args, **kwargs) -> None: ...


class SHiPMemRP(SHiPRP):
    shct_size: Any
    insertion_threshold: Any
    num_bits: Any
    hit_priority: Any
    btp: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SHiPPCRP(SHiPRP):
    shct_size: Any
    insertion_threshold: Any
    num_bits: Any
    hit_priority: Any
    btp: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SHiPRP(BRRIPRP):
    shct_size: Any
    insertion_threshold: Any
    num_bits: Any
    hit_priority: Any
    btp: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SIMD_Unit(FUDesc):
    count: Any
    opList: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SMTFetchPolicy(ScopedEnum):

    def __init__(self, *args, **kwargs) -> None: ...


class SMTQueuePolicy(ScopedEnum):

    def __init__(self, *args, **kwargs) -> None: ...


class STeMSPrefetcher(QueuedPrefetcher):
    spatial_region_size: Any
    active_generation_table_entries: Any
    active_generation_table_assoc: Any
    active_generation_table_indexing_policy: Any
    active_generation_table_replacement_policy: Any
    pattern_sequence_table_entries: Any
    pattern_sequence_table_assoc: Any
    pattern_sequence_table_indexing_policy: Any
    pattern_sequence_table_replacement_policy: Any
    region_miss_order_buffer_entries: Any
    add_duplicate_entries_to_rmob: Any
    reconstruction_entries: Any
    latency: Any
    queue_size: Any
    max_prefetch_requests_with_pending_translation: Any
    queue_squash: Any
    queue_filter: Any
    cache_snoop: Any
    tag_prefetch: Any
    throttle_control_percentage: Any
    sys: Any
    block_size: Any
    on_miss: Any
    on_read: Any
    on_write: Any
    on_data: Any
    on_inst: Any
    prefetch_on_access: Any
    prefetch_on_pf_hit: Any
    use_virtual_addresses: Any
    page_bytes: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class ScopedEnum(Enum):

    def __init__(self, *args, **kwargs) -> None: ...


class SecondChanceRP(FIFORP):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SectorTags(BaseTags):
    assoc: Any
    num_blocks_per_sector: Any
    replacement_policy: Any
    system: Any
    size: Any
    block_size: Any
    tag_latency: Any
    warmup_percentage: Any
    sequential_access: Any
    indexing_policy: Any
    partitioning_manager: Any
    entry_size: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SerialDevice(SimObject):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SerialLink(ClockedObject):
    req_size: Any
    resp_size: Any
    delay: Any
    ranges: Any
    num_lanes: Any
    link_speed: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SerialNullDevice(SerialDevice):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SeriesRequestGenerator(DirectedGenerator):
    addr_increment_size: Any
    num_series: Any
    percent_writes: Any
    num_cpus: Any
    system: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SetAssociative(BaseIndexingPolicy):
    size: Any
    entry_size: Any
    assoc: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SharedMemoryServer(SimObject):
    system: Any
    server_path: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SignaturePathPrefetcher(QueuedPrefetcher):
    signature_shift: Any
    signature_bits: Any
    signature_table_entries: Any
    signature_table_assoc: Any
    signature_table_indexing_policy: Any
    signature_table_replacement_policy: Any
    num_counter_bits: Any
    pattern_table_entries: Any
    pattern_table_assoc: Any
    strides_per_pattern_entry: Any
    pattern_table_indexing_policy: Any
    pattern_table_replacement_policy: Any
    prefetch_confidence_threshold: Any
    lookahead_confidence_threshold: Any
    latency: Any
    queue_size: Any
    max_prefetch_requests_with_pending_translation: Any
    queue_squash: Any
    queue_filter: Any
    cache_snoop: Any
    tag_prefetch: Any
    throttle_control_percentage: Any
    sys: Any
    block_size: Any
    on_miss: Any
    on_read: Any
    on_write: Any
    on_data: Any
    on_inst: Any
    prefetch_on_access: Any
    prefetch_on_pf_hit: Any
    use_virtual_addresses: Any
    page_bytes: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SignaturePathPrefetcherV2(SignaturePathPrefetcher):
    global_history_register_entries: Any
    global_history_register_indexing_policy: Any
    global_history_register_replacement_policy: Any
    signature_shift: Any
    signature_bits: Any
    signature_table_entries: Any
    signature_table_assoc: Any
    signature_table_indexing_policy: Any
    signature_table_replacement_policy: Any
    num_counter_bits: Any
    pattern_table_entries: Any
    pattern_table_assoc: Any
    strides_per_pattern_entry: Any
    pattern_table_indexing_policy: Any
    pattern_table_replacement_policy: Any
    prefetch_confidence_threshold: Any
    lookahead_confidence_threshold: Any
    latency: Any
    queue_size: Any
    max_prefetch_requests_with_pending_translation: Any
    queue_squash: Any
    queue_filter: Any
    cache_snoop: Any
    tag_prefetch: Any
    throttle_control_percentage: Any
    sys: Any
    block_size: Any
    on_miss: Any
    on_read: Any
    on_write: Any
    on_data: Any
    on_inst: Any
    prefetch_on_access: Any
    prefetch_on_pf_hit: Any
    use_virtual_addresses: Any
    page_bytes: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SimObject:
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SimObjectVector(VectorParamValue):

    def __init__(self, *args, **kwargs) -> None: ...


class SimPoint(ProbeListenerObject):
    interval: Any
    profile_file: Any
    manager: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SimpleBTB(BranchTargetBuffer):
    numEntries: Any
    tagBits: Any
    instShiftAmt: Any
    associativity: Any
    btbReplPolicy: Any
    btbIndexingPolicy: Any
    numThreads: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SimpleCache(ClockedObject):
    latency: Any
    size: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SimpleDisk(SimObject):
    disk: Any
    system: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SimpleExtLink(BasicExtLink):
    ext_node: Any
    int_node: Any
    link_id: Any
    latency: Any
    bandwidth_factor: Any
    weight: Any
    supported_vnets: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SimpleIndirectPredictor(IndirectPredictor):
    indirectHashGHR: Any
    indirectHashTargets: Any
    indirectSets: Any
    indirectWays: Any
    indirectTagSize: Any
    indirectPathLength: Any
    speculativePathLength: Any
    indirectGHRBits: Any
    instShiftAmt: Any
    numThreads: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SimpleIntLink(BasicIntLink):
    buffers: Any
    src_node: Any
    dst_node: Any
    src_outport: Any
    dst_inport: Any
    link_id: Any
    latency: Any
    bandwidth_factor: Any
    weight: Any
    supported_vnets: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SimpleMemDelay(MemDelay):
    read_req: Any
    read_resp: Any
    write_req: Any
    write_resp: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SimpleMemobj(SimObject):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SimpleMemory(AbstractMemory):
    latency: Any
    latency_var: Any
    bandwidth: Any
    range: Any
    null: Any
    in_addr_map: Any
    kvm_map: Any
    conf_table_reported: Any
    image_file: Any
    writeable: Any
    collect_stats: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SimpleNetwork(RubyNetwork):
    buffer_size: Any
    endpoint_bandwidth: Any
    physical_vnets_channels: Any
    physical_vnets_bandwidth: Any
    topology: Any
    number_of_virtual_networks: Any
    control_msg_size: Any
    ruby_system: Any
    routers: Any
    netifs: Any
    ext_links: Any
    int_links: Any
    data_msg_size: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SimpleObject(SimObject):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SimpleTrace(ProbeListenerObject):
    manager: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SimpleUart(Uart):
    byte_order: Any
    pio_size: Any
    end_on_eot: Any
    platform: Any
    device: Any
    pio_addr: Any
    pio_latency: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Sinic(EtherDevBase):
    rx_max_copy: Any
    tx_max_copy: Any
    rx_max_intr: Any
    rx_fifo_threshold: Any
    rx_fifo_low_mark: Any
    tx_fifo_high_mark: Any
    tx_fifo_threshold: Any
    virtual_count: Any
    zero_copy_size: Any
    zero_copy_threshold: Any
    zero_copy: Any
    delay_copy: Any
    virtual_addr: Any
    hardware_address: Any
    dma_read_delay: Any
    dma_read_factor: Any
    dma_write_delay: Any
    dma_write_factor: Any
    rx_delay: Any
    tx_delay: Any
    rx_fifo_size: Any
    tx_fifo_size: Any
    rx_filter: Any
    intr_delay: Any
    rx_thread: Any
    tx_thread: Any
    rss: Any
    BAR0: Any
    BAR1: Any
    BAR2: Any
    BAR3: Any
    BAR4: Any
    BAR5: Any
    CardbusCIS: Any
    SubsystemID: Any
    SubsystemVendorID: Any
    ExpansionROM: Any
    MaximumLatency: Any
    MinimumGrant: Any
    upstream: Any
    pci_dev: Any
    pci_func: Any
    pio_latency: Any
    config_latency: Any
    VendorID: Any
    DeviceID: Any
    Command: Any
    Status: Any
    Revision: Any
    ProgIF: Any
    SubClassCode: Any
    ClassCode: Any
    CacheLineSize: Any
    LatencyTimer: Any
    HeaderType: Any
    BIST: Any
    CapabilityPtr: Any
    InterruptLine: Any
    InterruptPin: Any
    PMCAPBaseOffset: Any
    PMCAPNextCapability: Any
    PMCAPCapId: Any
    PMCAPCapabilities: Any
    PMCAPCtrlStatus: Any
    MSICAPBaseOffset: Any
    MSICAPNextCapability: Any
    MSICAPCapId: Any
    MSICAPMsgCtrl: Any
    MSICAPMsgAddr: Any
    MSICAPMsgUpperAddr: Any
    MSICAPMsgData: Any
    MSICAPMaskBits: Any
    MSICAPPendingBits: Any
    MSIXCAPBaseOffset: Any
    MSIXCAPNextCapability: Any
    MSIXCAPCapId: Any
    MSIXMsgCtrl: Any
    MSIXTableOffset: Any
    MSIXPbaOffset: Any
    PXCAPBaseOffset: Any
    PXCAPNextCapability: Any
    PXCAPCapId: Any
    PXCAPCapabilities: Any
    PXCAPDevCapabilities: Any
    PXCAPDevCtrl: Any
    PXCAPDevStatus: Any
    PXCAPLinkCap: Any
    PXCAPLinkCtrl: Any
    PXCAPLinkStatus: Any
    PXCAPSlotCap: Any
    PXCAPSlotCtrl: Any
    PXCAPSlotStatus: Any
    PXCAPRootCap: Any
    PXCAPRootCtrl: Any
    PXCAPRootStatus: Any
    PXCAPDevCap2: Any
    PXCAPDevCtrl2: Any
    PXCAPDevStatus2: Any
    PXCAPLinkCap2: Any
    PXCAPLinkCtrl2: Any
    PXCAPLinkStatus2: Any
    PXCAPSlotCap2: Any
    PXCAPSlotCtrl2: Any
    PXCAPSlotStatus2: Any
    sid: Any
    ssid: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SkewedAssociative(BaseIndexingPolicy):
    size: Any
    entry_size: Any
    assoc: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SlavePort(Port):

    def __init__(self, *args, **kwargs) -> None: ...


class SlimAMPMPrefetcher(QueuedPrefetcher):
    ampm: Any
    dcpt: Any
    latency: Any
    queue_size: Any
    max_prefetch_requests_with_pending_translation: Any
    queue_squash: Any
    queue_filter: Any
    cache_snoop: Any
    tag_prefetch: Any
    throttle_control_percentage: Any
    sys: Any
    block_size: Any
    on_miss: Any
    on_read: Any
    on_write: Any
    on_data: Any
    on_inst: Any
    prefetch_on_access: Any
    prefetch_on_pf_hit: Any
    use_virtual_addresses: Any
    page_bytes: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SlimAccessMapPatternMatching(AccessMapPatternMatching):
    block_size: Any
    limit_stride: Any
    start_degree: Any
    hot_zone_size: Any
    access_map_table_entries: Any
    access_map_table_assoc: Any
    access_map_table_indexing_policy: Any
    access_map_table_replacement_policy: Any
    high_coverage_threshold: Any
    low_coverage_threshold: Any
    high_accuracy_threshold: Any
    low_accuracy_threshold: Any
    high_cache_hit_threshold: Any
    low_cache_hit_threshold: Any
    epoch_cycles: Any
    offchip_memory_latency: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SlimDeltaCorrelatingPredictionTables(DeltaCorrelatingPredictionTables):
    deltas_per_entry: Any
    delta_bits: Any
    delta_mask_bits: Any
    table_entries: Any
    table_assoc: Any
    table_indexing_policy: Any
    table_replacement_policy: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SmsPrefetcher(QueuedPrefetcher):
    ft_size: Any
    pht_size: Any
    region_size: Any
    latency: Any
    queue_size: Any
    max_prefetch_requests_with_pending_translation: Any
    queue_squash: Any
    queue_filter: Any
    cache_snoop: Any
    tag_prefetch: Any
    throttle_control_percentage: Any
    sys: Any
    block_size: Any
    on_miss: Any
    on_read: Any
    on_write: Any
    on_data: Any
    on_inst: Any
    prefetch_on_access: Any
    prefetch_on_pf_hit: Any
    use_virtual_addresses: Any
    page_bytes: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SnoopFilter(SimObject):
    lookup_latency: Any
    system: Any
    max_capacity: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SouthBridge(SimObject):
    pic1: Any
    pic2: Any
    cmos: Any
    dma1: Any
    keyboard: Any
    pit: Any
    speaker: Any
    io_apic: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SpatterGen(ClockedObject):
    system: Any
    processing_mode: Any
    int_regfile_size: Any
    fp_regfile_size: Any
    request_gen_latency: Any
    request_gen_rate: Any
    request_buffer_entries: Any
    send_rate: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SpatterKernelType(Enum):

    def __init__(self, *args, **kwargs) -> None: ...


class SpatterProcessingMode(Enum):

    def __init__(self, *args, **kwargs) -> None: ...


class SrcClockDomain(ClockDomain):
    clock: Any
    voltage_domain: Any
    domain_id: Any
    init_perf_level: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class StackDistProbe(BaseMemProbe):
    system: Any
    line_size: Any
    verify: Any
    linear_hist_bins: Any
    disable_linear_hists: Any
    log_hist_bins: Any
    disable_log_hists: Any
    manager: Any
    probe_name: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class StaticInstFlags(Enum):

    def __init__(self, *args, **kwargs) -> None: ...


class StatisticalCorrector(SimObject):
    instShiftAmt: Any
    numEntriesFirstLocalHistories: Any
    bwnb: Any
    bwm: Any
    logBwnb: Any
    bwWeightInitValue: Any
    lnb: Any
    lm: Any
    logLnb: Any
    lWeightInitValue: Any
    inb: Any
    im: Any
    logInb: Any
    iWeightInitValue: Any
    logBias: Any
    logSizeUp: Any
    chooserConfWidth: Any
    updateThresholdWidth: Any
    pUpdateThresholdWidth: Any
    extraWeightsWidth: Any
    scCountersWidth: Any
    initialUpdateThresholdValue: Any
    speculativeHistUpdate: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class StreamGenType(ScopedEnum):

    def __init__(self, *args, **kwargs) -> None: ...


class StridePrefetcher(QueuedPrefetcher):
    confidence_counter_bits: Any
    initial_confidence: Any
    confidence_threshold: Any
    use_requestor_id: Any
    use_cache_line_address: Any
    degree: Any
    distance: Any
    table_assoc: Any
    table_entries: Any
    table_indexing_policy: Any
    table_replacement_policy: Any
    latency: Any
    queue_size: Any
    max_prefetch_requests_with_pending_translation: Any
    queue_squash: Any
    queue_filter: Any
    cache_snoop: Any
    tag_prefetch: Any
    throttle_control_percentage: Any
    sys: Any
    block_size: Any
    on_miss: Any
    on_read: Any
    on_write: Any
    on_data: Any
    on_inst: Any
    prefetch_on_access: Any
    prefetch_on_pf_hit: Any
    use_virtual_addresses: Any
    page_bytes: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class StridePrefetcherHashedSetAssociative(TaggedSetAssociative):
    size: Any
    entry_size: Any
    assoc: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class String(ParamValue, str):

    def __init__(self, *args, **kwargs) -> None: ...


class StubWorkload(Workload):
    entry: Any
    byte_order: Any
    wait_for_remote_gdb: Any
    remote_gdb_port: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SubSystem(SimObject):
    thermal_domain: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Switch(BasicRouter):
    virt_nets: Any
    int_routing_latency: Any
    ext_routing_latency: Any
    port_buffers: Any
    routing_unit: Any
    router_id: Any
    latency: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SwitchPortBuffer(MessageBuffer):
    ordered: Any
    buffer_size: Any
    randomization: Any
    allow_zero_latency: Any
    max_dequeue_rate: Any
    routing_priority: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SysBridge(SimObject):
    source: Any
    target: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class System(SimObject):
    memories: Any
    mem_mode: Any
    thermal_model: Any
    thermal_components: Any
    mmap_using_noreserve: Any
    mem_ranges: Any
    external_memory_ranges: Any
    shadow_rom_ranges: Any
    shared_backstore: Any
    auto_unlink_shared_backstore: Any
    cache_line_size: Any
    redirect_paths: Any
    exit_on_work_items: Any
    work_item_id: Any
    num_work_ids: Any
    work_begin_cpu_id_exit: Any
    work_begin_ckpt_count: Any
    work_begin_exit_count: Any
    work_end_ckpt_count: Any
    work_end_exit_count: Any
    work_cpus_ckpt_count: Any
    workload: Any
    init_param: Any
    readfile: Any
    symbolfile: Any
    multi_thread: Any
    m5ops_base: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SystemC_Kernel(SimObject):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SystemC_ScModule(SystemC_ScObject):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SystemC_ScObject(SimObject):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class SystemXBar(CoherentXBar):
    snoop_response_latency: Any
    snoop_filter: Any
    max_outstanding_snoops: Any
    max_routing_table_size: Any
    point_of_coherency: Any
    point_of_unification: Any
    system: Any
    frontend_latency: Any
    forward_latency: Any
    response_latency: Any
    header_latency: Any
    width: Any
    use_default_range: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class System_Unit(FUDesc):
    count: Any
    opList: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TAGE(ConditionalPredictor):
    tage: Any
    numThreads: Any
    instShiftAmt: Any
    speculativeHistUpdate: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TAGEBase(SimObject):
    numThreads: Any
    instShiftAmt: Any
    nHistoryTables: Any
    minHist: Any
    maxHist: Any
    tagTableTagWidths: Any
    logTagTableSizes: Any
    logRatioBiModalHystEntries: Any
    tagTableCounterBits: Any
    tagTableUBits: Any
    histBufferSize: Any
    pathHistBits: Any
    logUResetPeriod: Any
    numUseAltOnNa: Any
    initialTCounterValue: Any
    useAltOnNaBits: Any
    maxNumAlloc: Any
    noSkip: Any
    speculativeHistUpdate: Any
    takenOnlyHistory: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TAGE_SC_L(LTAGE):
    statistical_corrector: Any
    loop_predictor: Any
    tage: Any
    numThreads: Any
    instShiftAmt: Any
    speculativeHistUpdate: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TAGE_SC_L_64KB(TAGE_SC_L):
    statistical_corrector: Any
    loop_predictor: Any
    tage: Any
    numThreads: Any
    instShiftAmt: Any
    speculativeHistUpdate: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TAGE_SC_L_64KB_LoopPredictor(TAGE_SC_L_LoopPredictor):
    logSizeLoopPred: Any
    withLoopBits: Any
    loopTableAgeBits: Any
    loopTableConfidenceBits: Any
    loopTableTagBits: Any
    loopTableIterBits: Any
    logLoopTableAssoc: Any
    useSpeculation: Any
    useHashing: Any
    useDirectionBit: Any
    restrictAllocation: Any
    initialLoopIter: Any
    initialLoopAge: Any
    optionalAgeReset: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TAGE_SC_L_64KB_StatisticalCorrector(StatisticalCorrector):
    pnb: Any
    pm: Any
    logPnb: Any
    snb: Any
    sm: Any
    logSnb: Any
    tnb: Any
    tm: Any
    logTnb: Any
    imnb: Any
    imm: Any
    logImnb: Any
    numEntriesSecondLocalHistories: Any
    numEntriesThirdLocalHistories: Any
    instShiftAmt: Any
    numEntriesFirstLocalHistories: Any
    bwnb: Any
    bwm: Any
    logBwnb: Any
    bwWeightInitValue: Any
    lnb: Any
    lm: Any
    logLnb: Any
    lWeightInitValue: Any
    inb: Any
    im: Any
    logInb: Any
    iWeightInitValue: Any
    logBias: Any
    logSizeUp: Any
    chooserConfWidth: Any
    updateThresholdWidth: Any
    pUpdateThresholdWidth: Any
    extraWeightsWidth: Any
    scCountersWidth: Any
    initialUpdateThresholdValue: Any
    speculativeHistUpdate: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TAGE_SC_L_8KB(TAGE_SC_L):
    statistical_corrector: Any
    loop_predictor: Any
    tage: Any
    numThreads: Any
    instShiftAmt: Any
    speculativeHistUpdate: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TAGE_SC_L_8KB_LoopPredictor(TAGE_SC_L_LoopPredictor):
    logSizeLoopPred: Any
    withLoopBits: Any
    loopTableAgeBits: Any
    loopTableConfidenceBits: Any
    loopTableTagBits: Any
    loopTableIterBits: Any
    logLoopTableAssoc: Any
    useSpeculation: Any
    useHashing: Any
    useDirectionBit: Any
    restrictAllocation: Any
    initialLoopIter: Any
    initialLoopAge: Any
    optionalAgeReset: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TAGE_SC_L_8KB_StatisticalCorrector(StatisticalCorrector):
    gnb: Any
    gm: Any
    logGnb: Any
    instShiftAmt: Any
    numEntriesFirstLocalHistories: Any
    bwnb: Any
    bwm: Any
    logBwnb: Any
    bwWeightInitValue: Any
    lnb: Any
    lm: Any
    logLnb: Any
    lWeightInitValue: Any
    inb: Any
    im: Any
    logInb: Any
    iWeightInitValue: Any
    logBias: Any
    logSizeUp: Any
    chooserConfWidth: Any
    updateThresholdWidth: Any
    pUpdateThresholdWidth: Any
    extraWeightsWidth: Any
    scCountersWidth: Any
    initialUpdateThresholdValue: Any
    speculativeHistUpdate: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TAGE_SC_L_LoopPredictor(LoopPredictor):
    logSizeLoopPred: Any
    withLoopBits: Any
    loopTableAgeBits: Any
    loopTableConfidenceBits: Any
    loopTableTagBits: Any
    loopTableIterBits: Any
    logLoopTableAssoc: Any
    useSpeculation: Any
    useHashing: Any
    useDirectionBit: Any
    restrictAllocation: Any
    initialLoopIter: Any
    initialLoopAge: Any
    optionalAgeReset: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TAGE_SC_L_TAGE(TAGEBase):
    logTagTableSize: Any
    shortTagsTageFactor: Any
    longTagsTageFactor: Any
    shortTagsSize: Any
    longTagsSize: Any
    firstLongTagTable: Any
    truncatePathHist: Any
    numThreads: Any
    instShiftAmt: Any
    nHistoryTables: Any
    minHist: Any
    maxHist: Any
    tagTableTagWidths: Any
    logTagTableSizes: Any
    logRatioBiModalHystEntries: Any
    tagTableCounterBits: Any
    tagTableUBits: Any
    histBufferSize: Any
    pathHistBits: Any
    logUResetPeriod: Any
    numUseAltOnNa: Any
    initialTCounterValue: Any
    useAltOnNaBits: Any
    maxNumAlloc: Any
    noSkip: Any
    speculativeHistUpdate: Any
    takenOnlyHistory: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TAGE_SC_L_TAGE_64KB(TAGE_SC_L_TAGE):
    logTagTableSize: Any
    shortTagsTageFactor: Any
    longTagsTageFactor: Any
    shortTagsSize: Any
    longTagsSize: Any
    firstLongTagTable: Any
    truncatePathHist: Any
    numThreads: Any
    instShiftAmt: Any
    nHistoryTables: Any
    minHist: Any
    maxHist: Any
    tagTableTagWidths: Any
    logTagTableSizes: Any
    logRatioBiModalHystEntries: Any
    tagTableCounterBits: Any
    tagTableUBits: Any
    histBufferSize: Any
    pathHistBits: Any
    logUResetPeriod: Any
    numUseAltOnNa: Any
    initialTCounterValue: Any
    useAltOnNaBits: Any
    maxNumAlloc: Any
    noSkip: Any
    speculativeHistUpdate: Any
    takenOnlyHistory: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TAGE_SC_L_TAGE_8KB(TAGE_SC_L_TAGE):
    logTagTableSize: Any
    shortTagsTageFactor: Any
    longTagsTageFactor: Any
    shortTagsSize: Any
    longTagsSize: Any
    firstLongTagTable: Any
    truncatePathHist: Any
    numThreads: Any
    instShiftAmt: Any
    nHistoryTables: Any
    minHist: Any
    maxHist: Any
    tagTableTagWidths: Any
    logTagTableSizes: Any
    logRatioBiModalHystEntries: Any
    tagTableCounterBits: Any
    tagTableUBits: Any
    histBufferSize: Any
    pathHistBits: Any
    logUResetPeriod: Any
    numUseAltOnNa: Any
    initialTCounterValue: Any
    useAltOnNaBits: Any
    maxNumAlloc: Any
    noSkip: Any
    speculativeHistUpdate: Any
    takenOnlyHistory: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TaggedIndexingPolicy(SimObject):
    assoc: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TaggedPrefetcher(QueuedPrefetcher):
    degree: Any
    latency: Any
    queue_size: Any
    max_prefetch_requests_with_pending_translation: Any
    queue_squash: Any
    queue_filter: Any
    cache_snoop: Any
    tag_prefetch: Any
    throttle_control_percentage: Any
    sys: Any
    block_size: Any
    on_miss: Any
    on_read: Any
    on_write: Any
    on_data: Any
    on_inst: Any
    prefetch_on_access: Any
    prefetch_on_pf_hit: Any
    use_virtual_addresses: Any
    page_bytes: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TaggedSetAssociative(TaggedIndexingPolicy):
    size: Any
    entry_size: Any
    assoc: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TargetProvider(Enum):

    def __init__(self, *args, **kwargs) -> None: ...


class TcpPort(CheckedInt):

    def __init__(self, *args, **kwargs) -> None: ...


class Temperature(ParamValue):

    def __init__(self, *args, **kwargs) -> None: ...


class Terminal(SerialDevice):
    port: Any
    number: Any
    outfile: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TerminalDump(ScopedEnum):

    def __init__(self, *args, **kwargs) -> None: ...


class ThermalCapacitor(SimObject):
    capacitance: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class ThermalDomain(SimObject):
    initial_temperature: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class ThermalModel(ClockedObject):
    step: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class ThermalNode(SimObject):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class ThermalReference(SimObject):
    temperature: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class ThermalResistor(SimObject):
    resistance: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class ThreadBridge(SimObject):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class ThreadPolicy(Enum):

    def __init__(self, *args, **kwargs) -> None: ...


class Tick(CheckedInt):

    def __init__(self, *args, **kwargs) -> None: ...


class TickedObject(ClockedObject):
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Time(ParamValue):

    def __init__(self, *args, **kwargs) -> None: ...


class TimingExpr(SimObject):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TimingExpr0(TimingExprLiteral):
    value: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TimingExprBin(TimingExpr):
    op: Any
    left: Any
    right: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TimingExprIf(TimingExpr):
    cond: Any
    trueExpr: Any
    falseExpr: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TimingExprLet(TimingExpr):
    defns: Any
    expr: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TimingExprLiteral(TimingExpr):
    value: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TimingExprOp(Enum):

    def __init__(self, *args, **kwargs) -> None: ...


class TimingExprRef(TimingExpr):
    index: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TimingExprSrcReg(TimingExpr):
    index: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TimingExprUn(TimingExpr):
    op: Any
    arg: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TimingSimpleCPU(BaseTimingSimpleCPU, X86CPU):
    branchPred: Any
    system: Any
    cpu_id: Any
    socket_id: Any
    numThreads: Any
    pwr_gating_latency: Any
    power_gating_on_idle: Any
    function_trace: Any
    function_trace_start: Any
    checker: Any
    syscallRetryLatency: Any
    do_checkpoint_insts: Any
    do_statistics_insts: Any
    workload: Any
    mmu: Any
    interrupts: Any
    isa: Any
    decoder: Any
    max_insts_all_threads: Any
    max_insts_any_thread: Any
    simpoint_start_insts: Any
    progress_interval: Any
    switched_out: Any
    tracer: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TlmInitiatorSocket(Port):

    def __init__(self, *args, **kwargs) -> None: ...


class TlmTargetSocket(Port):

    def __init__(self, *args, **kwargs) -> None: ...


class TlmToGem5Bridge128(TlmToGem5BridgeBase):
    system: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TlmToGem5Bridge256(TlmToGem5BridgeBase):
    system: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TlmToGem5Bridge32(TlmToGem5BridgeBase):
    system: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TlmToGem5Bridge512(TlmToGem5BridgeBase):
    system: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TlmToGem5Bridge64(TlmToGem5BridgeBase):
    system: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TlmToGem5BridgeBase(SystemC_ScModule):
    system: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TournamentBP(ConditionalPredictor):
    localPredictorSize: Any
    localCtrBits: Any
    localHistoryTableSize: Any
    globalPredictorSize: Any
    globalCtrBits: Any
    choicePredictorSize: Any
    choiceCtrBits: Any
    numThreads: Any
    instShiftAmt: Any
    speculativeHistUpdate: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TraceCPU(ClockedObject):
    system: Any
    instTraceFile: Any
    dataTraceFile: Any
    sizeStoreBuffer: Any
    sizeLoadBuffer: Any
    sizeROB: Any
    freqMultiplier: Any
    enableEarlyExit: Any
    progressMsgInterval: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TrafficGen(BaseTrafficGen):
    config_file: Any
    system: Any
    elastic_req: Any
    max_outstanding_reqs: Any
    progress_check: Any
    stream_gen: Any
    sids: Any
    ssids: Any
    cpu_id: Any
    socket_id: Any
    numThreads: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TreePLRURP(BaseReplacementPolicy):
    num_leaves: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class TypeTLB(ScopedEnum):

    def __init__(self, *args, **kwargs) -> None: ...


class UInt16(CheckedInt):

    def __init__(self, *args, **kwargs) -> None: ...


class UInt32(CheckedInt):

    def __init__(self, *args, **kwargs) -> None: ...


class UInt64(CheckedInt):

    def __init__(self, *args, **kwargs) -> None: ...


class UInt8(CheckedInt):

    def __init__(self, *args, **kwargs) -> None: ...


class Uart(BasicPioDevice):
    platform: Any
    device: Any
    pio_addr: Any
    pio_latency: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Uart8250(Uart):
    pio_size: Any
    platform: Any
    device: Any
    pio_addr: Any
    pio_latency: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class UdpPort(CheckedInt):

    def __init__(self, *args, **kwargs) -> None: ...


class Unsigned(CheckedInt):

    def __init__(self, *args, **kwargs) -> None: ...


class VectorEtherInt(VectorPort):

    def __init__(self, *args, **kwargs) -> None: ...


class VectorIntSinkPin(VectorPort):

    def __init__(self, *args, **kwargs) -> None: ...


class VectorIntSourcePin(VectorPort):

    def __init__(self, *args, **kwargs) -> None: ...


class VectorMasterPort(VectorPort):

    def __init__(self, *args, **kwargs) -> None: ...


class VectorParamDesc(SingleTypeParamDesc):

    def __init__(self, *args, **kwargs) -> None: ...


class VectorParamValue(list):

    def __init__(self, *args, **kwargs) -> None: ...


class VectorPort(Port):

    def __init__(self, *args, **kwargs) -> None: ...


class VectorRequestPort(VectorPort):

    def __init__(self, *args, **kwargs) -> None: ...


class VectorResetRequestPort(VectorPort):

    def __init__(self, *args, **kwargs) -> None: ...


class VectorResetResponsePort(VectorPort):

    def __init__(self, *args, **kwargs) -> None: ...


class VectorResponsePort(VectorPort):

    def __init__(self, *args, **kwargs) -> None: ...


class VectorSlavePort(VectorPort):

    def __init__(self, *args, **kwargs) -> None: ...


class VectorTlmInitiatorSocket(VectorPort):

    def __init__(self, *args, **kwargs) -> None: ...


class VectorTlmTargetSocket(VectorPort):

    def __init__(self, *args, **kwargs) -> None: ...


class VirtIO9PBase(VirtIODeviceBase):
    queueSize: Any
    tag: Any
    subsystem: Any
    system: Any
    byte_order: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class VirtIO9PDiod(VirtIO9PProxy):
    diod: Any
    root: Any
    socketPath: Any
    queueSize: Any
    tag: Any
    subsystem: Any
    system: Any
    byte_order: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class VirtIO9PProxy(VirtIO9PBase):
    queueSize: Any
    tag: Any
    subsystem: Any
    system: Any
    byte_order: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class VirtIO9PSocket(VirtIO9PProxy):
    server: Any
    port: Any
    queueSize: Any
    tag: Any
    subsystem: Any
    system: Any
    byte_order: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class VirtIOBlock(VirtIODeviceBase):
    queueSize: Any
    image: Any
    subsystem: Any
    system: Any
    byte_order: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class VirtIOConsole(VirtIODeviceBase):
    qRecvSize: Any
    qTransSize: Any
    device: Any
    subsystem: Any
    system: Any
    byte_order: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class VirtIODeviceBase(SimObject):
    subsystem: Any
    system: Any
    byte_order: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class VirtIODummyDevice(VirtIODeviceBase):
    subsystem: Any
    system: Any
    byte_order: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class VirtIORng(VirtIODeviceBase):
    qSize: Any
    subsystem: Any
    system: Any
    byte_order: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class VncInput(SimObject):
    frame_capture: Any
    img_format: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class VncServer(VncInput):
    port: Any
    number: Any
    frame_capture: Any
    img_format: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Voltage(Float):

    def __init__(self, *args, **kwargs) -> None: ...


class VoltageDomain(SimObject):
    voltage: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class WayPartitioningPolicy(BasePartitioningPolicy):
    cache_associativity: Any
    allocations: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class WayPolicyAllocation(SimObject):
    partition_id: Any
    ways: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class WeightBased(BaseRoutingUnit):
    adaptive_routing: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class WeightedLRURP(LRURP):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class WideIO_200_1x128(DRAMInterface):
    page_policy: Any
    max_accesses_per_row: Any
    bank_groups_per_rank: Any
    enable_dram_powerdown: Any
    dll: Any
    tRCD: Any
    tRCD_WR: Any
    tCL: Any
    tCWL: Any
    tRP: Any
    tRAS: Any
    tWR: Any
    tRTP: Any
    tBURST_MAX: Any
    tBURST_MIN: Any
    tCCD_L: Any
    tCCD_L_WR: Any
    tRFC: Any
    tREFI: Any
    tWTR_L: Any
    tPPD: Any
    tAAD: Any
    two_cycle_activate: Any
    tRRD: Any
    tRRD_L: Any
    tXAW: Any
    activation_limit: Any
    tXP: Any
    tXPDLL: Any
    tXS: Any
    tXSDLL: Any
    beats_per_clock: Any
    data_clock_sync: Any
    IDD0: Any
    IDD02: Any
    IDD2P0: Any
    IDD2P02: Any
    IDD2P1: Any
    IDD2P12: Any
    IDD2N: Any
    IDD2N2: Any
    IDD3P0: Any
    IDD3P02: Any
    IDD3P1: Any
    IDD3P12: Any
    IDD3N: Any
    IDD3N2: Any
    IDD4R: Any
    IDD4R2: Any
    IDD4W: Any
    IDD4W2: Any
    IDD5: Any
    IDD52: Any
    IDD6: Any
    IDD62: Any
    VDD: Any
    VDD2: Any
    write_buffer_size: Any
    read_buffer_size: Any
    addr_mapping: Any
    device_size: Any
    device_bus_width: Any
    burst_length: Any
    device_rowbuffer_size: Any
    devices_per_rank: Any
    ranks_per_channel: Any
    banks_per_rank: Any
    tCK: Any
    tBURST: Any
    tWTR: Any
    tRTW: Any
    tCS: Any
    range: Any
    null: Any
    in_addr_map: Any
    kvm_map: Any
    conf_table_reported: Any
    image_file: Any
    writeable: Any
    collect_stats: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class Workload(SimObject):
    wait_for_remote_gdb: Any
    remote_gdb_port: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class WriteAllocator(SimObject):
    coalesce_limit: Any
    no_allocate_limit: Any
    delay_threshold: Any
    block_size: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class WritePort(FUDesc):
    count: Any
    opList: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86ACPIMadt(X86ACPISysDescTable):
    local_apic_address: Any
    flags: Any
    records: Any
    oem_id: Any
    oem_table_id: Any
    oem_revision: Any
    creator_id: Any
    creator_revision: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86ACPIMadtIOAPIC(X86ACPIMadtRecord):
    id: Any
    address: Any
    int_base: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86ACPIMadtIntSourceOverride(X86ACPIMadtRecord):
    bus_source: Any
    irq_source: Any
    sys_int: Any
    flags: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86ACPIMadtLAPIC(X86ACPIMadtRecord):
    acpi_processor_id: Any
    apic_id: Any
    flags: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86ACPIMadtLAPICOverride(X86ACPIMadtRecord):
    address: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86ACPIMadtNMI(X86ACPIMadtRecord):
    acpi_processor_id: Any
    flags: Any
    lint_no: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86ACPIMadtRecord(SimObject):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86ACPIRSDP(SimObject):
    oem_id: Any
    revision: Any
    rsdt: Any
    xsdt: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86ACPIRSDT(X86ACPISysDescTable):
    entries: Any
    oem_id: Any
    oem_table_id: Any
    oem_revision: Any
    creator_id: Any
    creator_revision: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86ACPISysDescTable(SimObject):
    oem_id: Any
    oem_table_id: Any
    oem_revision: Any
    creator_id: Any
    creator_revision: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86ACPIXSDT(X86ACPISysDescTable):
    entries: Any
    oem_id: Any
    oem_table_id: Any
    oem_revision: Any
    creator_id: Any
    creator_revision: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86AtomicSimpleCPU(BaseAtomicSimpleCPU, X86CPU):
    width: Any
    simulate_data_stalls: Any
    simulate_inst_stalls: Any
    branchPred: Any
    system: Any
    cpu_id: Any
    socket_id: Any
    numThreads: Any
    pwr_gating_latency: Any
    power_gating_on_idle: Any
    function_trace: Any
    function_trace_start: Any
    checker: Any
    syscallRetryLatency: Any
    do_checkpoint_insts: Any
    do_statistics_insts: Any
    workload: Any
    mmu: Any
    interrupts: Any
    isa: Any
    decoder: Any
    max_insts_all_threads: Any
    max_insts_any_thread: Any
    simpoint_start_insts: Any
    progress_interval: Any
    switched_out: Any
    tracer: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86BareMetalWorkload(Workload):
    wait_for_remote_gdb: Any
    remote_gdb_port: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86CPU:

    def __init__(self, *args, **kwargs) -> None: ...


class X86Decoder(InstDecoder):
    isa: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86E820Entry(SimObject):
    addr: Any
    size: Any
    range_type: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86E820Table(SimObject):
    entries: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86EmuLinux(SEWorkload):
    wait_for_remote_gdb: Any
    remote_gdb_port: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86FsLinux(X86FsWorkload):
    e820_table: Any
    exit_on_kernel_panic: Any
    exit_on_kernel_oops: Any
    on_panic: Any
    on_oops: Any
    smbios_table: Any
    intel_mp_pointer: Any
    intel_mp_table: Any
    acpi_description_table_pointer: Any
    enable_osxsave: Any
    object_file: Any
    extras: Any
    extras_addrs: Any
    addr_check: Any
    load_addr_mask: Any
    load_addr_offset: Any
    command_line: Any
    wait_for_remote_gdb: Any
    remote_gdb_port: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86FsWorkload(KernelWorkload):
    smbios_table: Any
    intel_mp_pointer: Any
    intel_mp_table: Any
    acpi_description_table_pointer: Any
    enable_osxsave: Any
    exit_on_kernel_panic: Any
    exit_on_kernel_oops: Any
    object_file: Any
    extras: Any
    extras_addrs: Any
    addr_check: Any
    load_addr_mask: Any
    load_addr_offset: Any
    command_line: Any
    on_panic: Any
    on_oops: Any
    wait_for_remote_gdb: Any
    remote_gdb_port: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86I8259CascadeMode(Enum):

    def __init__(self, *args, **kwargs) -> None: ...


class X86ISA(BaseISA):
    vendor_string: Any
    name_string: Any
    FamilyModelStepping: Any
    CacheParams: Any
    ExtendedFeatures: Any
    ExtendedState: Any
    FamilyModelSteppingBrandFeatures: Any
    L1CacheAndTLB: Any
    L2L3CacheAndL2TLB: Any
    APMInfo: Any
    LongModeAddressSize: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86IdeController(IdeController):
    disks: Any
    io_shift: Any
    ctrl_offset: Any
    BAR0: Any
    BAR1: Any
    BAR2: Any
    BAR3: Any
    BAR4: Any
    BAR5: Any
    CardbusCIS: Any
    SubsystemID: Any
    SubsystemVendorID: Any
    ExpansionROM: Any
    MaximumLatency: Any
    MinimumGrant: Any
    upstream: Any
    pci_dev: Any
    pci_func: Any
    pio_latency: Any
    config_latency: Any
    VendorID: Any
    DeviceID: Any
    Command: Any
    Status: Any
    Revision: Any
    ProgIF: Any
    SubClassCode: Any
    ClassCode: Any
    CacheLineSize: Any
    LatencyTimer: Any
    HeaderType: Any
    BIST: Any
    CapabilityPtr: Any
    InterruptLine: Any
    InterruptPin: Any
    PMCAPBaseOffset: Any
    PMCAPNextCapability: Any
    PMCAPCapId: Any
    PMCAPCapabilities: Any
    PMCAPCtrlStatus: Any
    MSICAPBaseOffset: Any
    MSICAPNextCapability: Any
    MSICAPCapId: Any
    MSICAPMsgCtrl: Any
    MSICAPMsgAddr: Any
    MSICAPMsgUpperAddr: Any
    MSICAPMsgData: Any
    MSICAPMaskBits: Any
    MSICAPPendingBits: Any
    MSIXCAPBaseOffset: Any
    MSIXCAPNextCapability: Any
    MSIXCAPCapId: Any
    MSIXMsgCtrl: Any
    MSIXTableOffset: Any
    MSIXPbaOffset: Any
    PXCAPBaseOffset: Any
    PXCAPNextCapability: Any
    PXCAPCapId: Any
    PXCAPCapabilities: Any
    PXCAPDevCapabilities: Any
    PXCAPDevCtrl: Any
    PXCAPDevStatus: Any
    PXCAPLinkCap: Any
    PXCAPLinkCtrl: Any
    PXCAPLinkStatus: Any
    PXCAPSlotCap: Any
    PXCAPSlotCtrl: Any
    PXCAPSlotStatus: Any
    PXCAPRootCap: Any
    PXCAPRootCtrl: Any
    PXCAPRootStatus: Any
    PXCAPDevCap2: Any
    PXCAPDevCtrl2: Any
    PXCAPDevStatus2: Any
    PXCAPLinkCap2: Any
    PXCAPLinkCtrl2: Any
    PXCAPLinkStatus2: Any
    PXCAPSlotCap2: Any
    PXCAPSlotCtrl2: Any
    PXCAPSlotStatus2: Any
    sid: Any
    ssid: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86IntMultDiv(IntMultDiv):
    count: Any
    opList: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86IntelMPAddrSpaceMapping(X86IntelMPExtConfigEntry):
    bus_id: Any
    address_type: Any
    address: Any
    length: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86IntelMPAddressType(Enum):

    def __init__(self, *args, **kwargs) -> None: ...


class X86IntelMPBaseConfigEntry(SimObject):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86IntelMPBus(X86IntelMPBaseConfigEntry):
    bus_id: Any
    bus_type: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86IntelMPBusHierarchy(X86IntelMPExtConfigEntry):
    bus_id: Any
    subtractive_decode: Any
    parent_bus: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86IntelMPCompatAddrSpaceMod(X86IntelMPExtConfigEntry):
    bus_id: Any
    add: Any
    range_list: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86IntelMPConfigTable(SimObject):
    spec_rev: Any
    oem_id: Any
    product_id: Any
    oem_table_addr: Any
    oem_table_size: Any
    local_apic: Any
    base_entries: Any
    ext_entries: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86IntelMPExtConfigEntry(SimObject):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86IntelMPFloatingPointer(SimObject):
    spec_rev: Any
    default_config: Any
    imcr_present: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86IntelMPIOAPIC(X86IntelMPBaseConfigEntry):
    id: Any
    version: Any
    enable: Any
    address: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86IntelMPIOIntAssignment(X86IntelMPBaseConfigEntry):
    interrupt_type: Any
    polarity: Any
    trigger: Any
    source_bus_id: Any
    source_bus_irq: Any
    dest_io_apic_id: Any
    dest_io_apic_intin: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86IntelMPInterruptType(Enum):

    def __init__(self, *args, **kwargs) -> None: ...


class X86IntelMPLocalIntAssignment(X86IntelMPBaseConfigEntry):
    interrupt_type: Any
    polarity: Any
    trigger: Any
    source_bus_id: Any
    source_bus_irq: Any
    dest_local_apic_id: Any
    dest_local_apic_intin: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86IntelMPPolarity(Enum):

    def __init__(self, *args, **kwargs) -> None: ...


class X86IntelMPProcessor(X86IntelMPBaseConfigEntry):
    local_apic_id: Any
    local_apic_version: Any
    enable: Any
    bootstrap: Any
    stepping: Any
    model: Any
    family: Any
    feature_flags: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86IntelMPRangeList(Enum):

    def __init__(self, *args, **kwargs) -> None: ...


class X86IntelMPTriggerMode(Enum):

    def __init__(self, *args, **kwargs) -> None: ...


class X86KvmCPU(BaseKvmCPU, X86CPU):
    useXSave: Any
    usePerf: Any
    useCoalescedMMIO: Any
    usePerfOverflow: Any
    alwaysSyncTC: Any
    hostFreq: Any
    hostFactor: Any
    system: Any
    cpu_id: Any
    socket_id: Any
    numThreads: Any
    pwr_gating_latency: Any
    power_gating_on_idle: Any
    function_trace: Any
    function_trace_start: Any
    checker: Any
    syscallRetryLatency: Any
    do_checkpoint_insts: Any
    do_statistics_insts: Any
    workload: Any
    mmu: Any
    interrupts: Any
    isa: Any
    decoder: Any
    max_insts_all_threads: Any
    max_insts_any_thread: Any
    simpoint_start_insts: Any
    progress_interval: Any
    switched_out: Any
    tracer: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86LocalApic(BaseInterrupts):
    int_latency: Any
    system: Any
    pio_latency: Any
    clk_domain: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86MMU(BaseMMU):
    itb: Any
    dtb: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86MinorCPU(BaseMinorCPU, X86CPU):
    threadPolicy: Any
    fetch1FetchLimit: Any
    fetch1LineSnapWidth: Any
    fetch1LineWidth: Any
    fetch1ToFetch2ForwardDelay: Any
    fetch1ToFetch2BackwardDelay: Any
    fetch2InputBufferSize: Any
    fetch2ToDecodeForwardDelay: Any
    fetch2CycleInput: Any
    decodeInputBufferSize: Any
    decodeToExecuteForwardDelay: Any
    decodeInputWidth: Any
    decodeCycleInput: Any
    executeInputWidth: Any
    executeCycleInput: Any
    executeIssueLimit: Any
    executeMemoryIssueLimit: Any
    executeCommitLimit: Any
    executeMemoryCommitLimit: Any
    executeInputBufferSize: Any
    executeMemoryWidth: Any
    executeMaxAccessesInMemory: Any
    executeLSQMaxStoreBufferStoresPerCycle: Any
    executeLSQRequestsQueueSize: Any
    executeLSQTransfersQueueSize: Any
    executeLSQStoreBufferSize: Any
    executeBranchDelay: Any
    executeFuncUnits: Any
    executeSetTraceTimeOnCommit: Any
    executeSetTraceTimeOnIssue: Any
    executeAllowEarlyMemoryIssue: Any
    enableIdling: Any
    branchPred: Any
    system: Any
    cpu_id: Any
    socket_id: Any
    numThreads: Any
    pwr_gating_latency: Any
    power_gating_on_idle: Any
    function_trace: Any
    function_trace_start: Any
    checker: Any
    syscallRetryLatency: Any
    do_checkpoint_insts: Any
    do_statistics_insts: Any
    workload: Any
    mmu: Any
    interrupts: Any
    isa: Any
    decoder: Any
    max_insts_all_threads: Any
    max_insts_any_thread: Any
    simpoint_start_insts: Any
    progress_interval: Any
    switched_out: Any
    tracer: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86NativeTrace(NativeTrace):
    disassembler: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86NonCachingSimpleCPU(BaseNonCachingSimpleCPU, X86CPU):
    width: Any
    simulate_data_stalls: Any
    simulate_inst_stalls: Any
    branchPred: Any
    system: Any
    cpu_id: Any
    socket_id: Any
    numThreads: Any
    pwr_gating_latency: Any
    power_gating_on_idle: Any
    function_trace: Any
    function_trace_start: Any
    checker: Any
    syscallRetryLatency: Any
    do_checkpoint_insts: Any
    do_statistics_insts: Any
    workload: Any
    mmu: Any
    interrupts: Any
    isa: Any
    decoder: Any
    max_insts_all_threads: Any
    max_insts_any_thread: Any
    simpoint_start_insts: Any
    progress_interval: Any
    switched_out: Any
    tracer: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86O3CPU(BaseO3CPU, X86CPU):
    activity: Any
    cacheStorePorts: Any
    cacheLoadPorts: Any
    fetchToBacDelay: Any
    decodeToFetchDelay: Any
    renameToFetchDelay: Any
    iewToFetchDelay: Any
    commitToFetchDelay: Any
    fetchWidth: Any
    fetchBufferSize: Any
    fetchQueueSize: Any
    renameToDecodeDelay: Any
    iewToDecodeDelay: Any
    commitToDecodeDelay: Any
    bacToFetchDelay: Any
    fetchToDecodeDelay: Any
    decodeWidth: Any
    iewToRenameDelay: Any
    commitToRenameDelay: Any
    decodeToRenameDelay: Any
    renameWidth: Any
    commitToIEWDelay: Any
    renameToIEWDelay: Any
    issueToExecuteDelay: Any
    dispatchWidth: Any
    issueWidth: Any
    wbWidth: Any
    iewToCommitDelay: Any
    renameToROBDelay: Any
    commitWidth: Any
    squashWidth: Any
    trapLatency: Any
    fetchTrapLatency: Any
    backComSize: Any
    forwardComSize: Any
    LQEntries: Any
    SQEntries: Any
    LSQDepCheckShift: Any
    LSQCheckLoads: Any
    store_set_clear_period: Any
    LFSTSize: Any
    SSITSize: Any
    SSITAssoc: Any
    SSITReplPolicy: Any
    SSITIndexingPolicy: Any
    numRobs: Any
    numPhysIntRegs: Any
    numPhysFloatRegs: Any
    numPhysVecRegs: Any
    numPhysVecPredRegs: Any
    numPhysMatRegs: Any
    numPhysCCRegs: Any
    instQueues: Any
    numROBEntries: Any
    smtNumFetchingThreads: Any
    smtFetchPolicy: Any
    smtLSQPolicy: Any
    smtLSQThreshold: Any
    smtROBPolicy: Any
    smtROBThreshold: Any
    smtCommitPolicy: Any
    branchPred: Any
    needsTSO: Any
    recvRespThrottling: Any
    recvRespMaxCachelines: Any
    recvRespBufferSize: Any
    decoupledFrontEnd: Any
    numFTQEntries: Any
    minInstSize: Any
    fetchTargetWidth: Any
    maxFTPerCycle: Any
    maxTakenPredPerCycle: Any
    system: Any
    cpu_id: Any
    socket_id: Any
    numThreads: Any
    pwr_gating_latency: Any
    power_gating_on_idle: Any
    function_trace: Any
    function_trace_start: Any
    checker: Any
    syscallRetryLatency: Any
    do_checkpoint_insts: Any
    do_statistics_insts: Any
    workload: Any
    mmu: Any
    interrupts: Any
    isa: Any
    decoder: Any
    max_insts_all_threads: Any
    max_insts_any_thread: Any
    simpoint_start_insts: Any
    progress_interval: Any
    switched_out: Any
    tracer: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86PagetableWalker(ClockedObject):
    system: Any
    num_squash_per_cycle: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86QemuFwCfg(QemuFwCfgIo):
    selector_addr: Any
    items: Any
    system: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86SMBiosBiosInformation(X86SMBiosSMBiosStructure):
    vendor: Any
    version: Any
    starting_addr_segment: Any
    release_date: Any
    rom_size: Any
    characteristics: Any
    characteristic_ext_bytes: Any
    major: Any
    minor: Any
    emb_cont_firmware_major: Any
    emb_cont_firmware_minor: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86SMBiosSMBiosStructure(SimObject):
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86SMBiosSMBiosTable(SimObject):
    major_version: Any
    minor_version: Any
    structures: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86TLB(BaseTLB):
    size: Any
    system: Any
    walker: Any
    entry_type: Any
    next_level: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class X86TimingSimpleCPU(BaseTimingSimpleCPU, X86CPU):
    branchPred: Any
    system: Any
    cpu_id: Any
    socket_id: Any
    numThreads: Any
    pwr_gating_latency: Any
    power_gating_on_idle: Any
    function_trace: Any
    function_trace_start: Any
    checker: Any
    syscallRetryLatency: Any
    do_checkpoint_insts: Any
    do_statistics_insts: Any
    workload: Any
    mmu: Any
    interrupts: Any
    isa: Any
    decoder: Any
    max_insts_all_threads: Any
    max_insts_any_thread: Any
    simpoint_start_insts: Any
    progress_interval: Any
    switched_out: Any
    tracer: Any
    clk_domain: Any
    power_model: Any
    power_state: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class ZeroCompressor(BaseDictionaryCompressor):
    dictionary_size: Any
    block_size: Any
    chunk_size_bits: Any
    size_threshold_percentage: Any
    comp_chunks_per_cycle: Any
    comp_extra_latency: Any
    decomp_chunks_per_cycle: Any
    decomp_extra_latency: Any
    eventq_index: Any

    def __init__(self, *args, **kwargs) -> None: ...


class abstractclassmethod(classmethod):

    def __init__(self, *args, **kwargs) -> None: ...


class abstractproperty(property):

    def __init__(self, *args, **kwargs) -> None: ...


class abstractstaticmethod(staticmethod):

    def __init__(self, *args, **kwargs) -> None: ...


