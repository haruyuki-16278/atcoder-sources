#include <stdio.h>

int main(void) {
    char name[11] = "\0";
    scanf("%s", name);
    name[0] += 32;

    printf("Of%s", name);
    return 0;
}