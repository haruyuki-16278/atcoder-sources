#include <stdio.h>

int main(void) {
    int h, w;
    scanf("%d %d", &h, &w);

    int i, j;
    for (i = 0; i < h; i++) {
        for (j = 0; j < w; j++) {
            int nexts = 4;
            if (i == 0 || i == h - 1) nexts--;
            if (j == 0 || j == w - 1) nexts--;
            if (h == 1) nexts--;
            if (w == 1) nexts--;
            printf("%d%s", nexts, j == w -1 ? "" : " ");
        }
        printf("\n");
    }

    return 0;
}