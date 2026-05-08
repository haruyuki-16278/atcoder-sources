#include <stdio.h>

int main(void) {
    int h = 0, w = 0, r = 0, c = 0;
    scanf("%d %d", &h, &w);
    scanf("%d %d", &r, &c);

    int diffs[5] = {0, 1, 0, -1, 0};
    int i = 0, cells = 0;
    for (i = 0; i < 4; i++) {
        int tr = r + diffs[i], tc = c + diffs[i + 1];
        // printf("%d, %d\n", tr, tc);
        if ((tr > 0 && tr <= h) && (tc > 0 && tc <= w)) {
            cells++;
        }
    }

    printf("%d", cells);
    return 0;
}