#include <stdio.h>
#include <string.h>

int main(void) {
    char x[6] = "\0", r[6] = "\0";
    scanf("%s", x);
    int len = strlen(x);

    int i, j;
    for (i = 0; i < len; i++) {
        int mini = 0;
        for (j = i; j < len; j++) {
            if (i == 0) {
                if (x[j] != '0' &&  x[j] < x[mini]) {
                    mini = j;
                }
            } else {
                if (x[j] < x[mini]) {
                    mini = j;
                }
        }
        r[i] = x[mini];
        x[mini] = '9';
        // printf("%s, %s\n", x, r);
    }
    printf("%s", r);

    return 0;
}