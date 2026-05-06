#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    scanf("%d", &n);
    char *s;
    s = malloc(sizeof(char) * n);
    scanf("%s", s);

    int i;
    int t = 0, a = 0;
    char latest = ' ';
    for (i = 0; i < n; i++) {
        if (s[i] == 'T') {
            t++;
            latest = 't';
        } else {
            a++;
            latest = 'a';
        }
    }

    if (a == t) {
        if (latest == 'a') {
            printf("T");
        } else {
            printf("A");
        }
    } else if (t > a) {
        printf("T");
    } else {
        printf("A");
    }

    free(s);
    return 0;
}