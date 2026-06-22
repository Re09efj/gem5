#define _GNU_SOURCE
#include <sched.h>
#include <stdio.h>

/*
 * NUMA CPU map: thread_id -> cpu_id
 *
 * Your NUMA layout:
 *   Node 0: CPU  0- 3 (P-cores), CPU  4- 7 (E-cores)
 *   Node 1: CPU  8-11 (P-cores), CPU 12-15 (E-cores)
 *
 * Swap the values below and recompile to change NUMA placement.
 *
 * Preset patterns (uncomment one):
 *
 * [A] All Node 0 (P-cores only, 4 threads):
 *   { 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3 }
 *
 * [B] All Node 1 (P-cores only, 4 threads):
 *   { 8, 9,10,11, 8, 9,10,11, 8, 9,10,11, 8, 9,10,11 }
 *
 * [C] Interleaved P-cores across nodes (8 threads):
 *   { 0, 8, 1, 9, 2,10, 3,11, 0, 8, 1, 9, 2,10, 3,11 }
 *
 * [D] Split: first half Node 0, second half Node 1 (8 threads):
 *   { 0, 1, 2, 3, 8, 9,10,11, 0, 1, 2, 3, 8, 9,10,11 }
 *
 * [E] Sequential all (16 threads):
 *   { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15 }
 */
static int cpu_map[16] = {
    0, 8, 1, 9, 2, 10, 3, 11,
    4, 12, 5, 13, 6, 14, 7, 15
};

/* Called from Fortran as: call set_affinity(myid)
 * gfortran passes integers by reference, hence int* */
void set_affinity_(int *thread_id)
{
    int tid = *thread_id;
    if (tid < 0 || tid >= 16) return;

    cpu_set_t cpuset;
    CPU_ZERO(&cpuset);
    CPU_SET(cpu_map[tid], &cpuset);

    if (sched_setaffinity(0, sizeof(cpu_set_t), &cpuset) != 0)
        fprintf(stderr, "[NUMA] sched_setaffinity failed: thread %d -> cpu %d\n",
                tid, cpu_map[tid]);
}
