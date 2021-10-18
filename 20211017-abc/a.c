#include <stdio.h>
 
int main(void) {
    int X;
    scanf("%d", &X);
 
    if (X % 100 == 0 && X > 0) {
        printf("Yes");
    }
    else {
        printf("No");
    }
 
    return 0;
}