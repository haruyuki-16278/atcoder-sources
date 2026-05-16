#include <stdio.h>
#include <string.h>

int main(void) {
    char str[500000 + 1] = "";
    scanf("%s", str);

    unsigned long long patterns = 0;
    int stln = strlen(str);
    int i;
    for (i = 0; i < stln; i++) {
        if (str[i] == 'C') {
            if (i + 1 <= (stln + 1) / 2) patterns += i + 1;
            else patterns += stln - i;
        }
    }
    printf("%llu", patterns);

    return 0;
}

