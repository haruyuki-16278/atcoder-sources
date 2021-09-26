#include <stdio.h>

int main(void){
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);

    int nc=c;
    while (nc <= 1000)
    {
        if(a <= nc && nc <= b){
            printf("\n%d", nc);
            return 0;
        }
        nc += c;
    }
    printf("%d", -1);
    return 0;
}