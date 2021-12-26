#include <stdio.h>

int main(void) {
    int X, Y;
    scanf("%d %d", &X, &Y);
    printf("%d", X < Y ? (Y-X)/10 + ((Y-X)%10 > 0) : 0);
    return 0;
}