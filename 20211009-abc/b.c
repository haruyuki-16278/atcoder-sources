#include <stdio.h>

int main(void) {
    int i;
    int n, p;
    int r=0;
    scanf("%d %d", &n, &p);
    int a;
    for(i=0; i<n; i++){
        scanf("%d", &a);
        r += a < p ? 1 : 0;
    }
    printf("%d", r);
}