#include <stdio.h>
#include <stdlib.h>

#define MATRIX_SIZE 20
#define REPEAT 13

int main(int argc, char* argv[]) {
    // gem5から cpu_id が argv[1] で渡される想定
    int cpu_id = (argc > 1) ? atoi(argv[1]) : 0;

    // スタック上に確保（SE modeではmallocも不安定な場合がある）
    static double a[MATRIX_SIZE][MATRIX_SIZE];
    static double b[MATRIX_SIZE][MATRIX_SIZE];
    static double c[MATRIX_SIZE][MATRIX_SIZE];

    for (int i = 0; i < MATRIX_SIZE; i++)
        for (int j = 0; j < MATRIX_SIZE; j++) {
            a[i][j] = i + j;
            b[i][j] = i - j;
        }

    for (int k = 0; k < REPEAT; k++)
        for (int i = 0; i < MATRIX_SIZE; i++)
            for (int j = 0; j < MATRIX_SIZE; j++) {
                c[i][j] = 0;
                for (int x = 0; x < MATRIX_SIZE; x++)
                    c[i][j] += a[i][x] * b[x][j];
            }

    printf("CPU %d: 計算完了\n", cpu_id);
    return 0;
}