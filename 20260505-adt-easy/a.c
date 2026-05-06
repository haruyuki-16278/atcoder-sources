#include <stdio.h>
#include <string.h>

int main(void) {
    char s[100];
    scanf("%s", s);

    int len = strlen(s);
    int i;
    for (i = len - 1; i >= 0; i--) {
        if (s[i] == 'a') {
            printf("%d", i + 1);
            return 0;
        }
    }
    
    printf("-1");
    return 0;
}