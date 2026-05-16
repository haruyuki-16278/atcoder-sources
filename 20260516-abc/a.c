#include <stdio.h>
#include <string.h>

int main(void) {
    char str[31] = "";
    int n;

    scanf("%s", str);
    scanf("%d", &n);

    // printf("%lu", strlen(str) - 2 * n);
    int i;
    for (i = n; i < strlen(str) - n; i++) {
        printf("%c", str[i]);
    }

    return 0;
}