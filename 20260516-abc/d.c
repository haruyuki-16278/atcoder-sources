#include <stdio.h>
#include <stdlib.h>

#define DEBUG 0

int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int main(void) {
    int q, x;

    scanf("%d", &x);
    scanf("%d", &q);

    int *bd;
    bd = (int *)malloc(sizeof(int) * q * 2 + 2);
    bd[0] = x;

    int i, j, k;
    int a, b;
    for (i = 0; i < q; i++) {
        scanf("%d %d", &a, &b);
        for (j = 0; i < i * 2 + 2; j++) {
            printf("fire");
            if (bd[j] <= a) {
                for (k = i * 2 + 1; k > j; k--) {
                    bd[k] = bd[k - 1];
                }
                bd[j] = a;
            }
            if (bd[j] <= b) {
                for (k = i * 2 + 1; k > j; k--) {
                    bd[k] = bd[k - 1];
                }
                bd[j] = a;
            }
        }

        if (DEBUG) {
            for (j = 0; j < i * 2 + 3; j++) {
                printf("%d, ", bd[j]);
            }
            printf("\n");
        }

        printf("%d\n", bd[i + 1]);
    }

    return 0;
}