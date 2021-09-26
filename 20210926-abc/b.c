#include <stdio.h>
#include <math.h>
void main(void){
    double k, a_k, b_k;
    scanf("%lf", &k);
    scanf("%lf %lf", &a_k, &b_k);

    double a=0, b=0;
    int i;
    for(i=0; pow(10, i)<=a_k; i++){
        // printf("a : %lf += %lf / %lf %% %lf * %lf = %lf\n", a, a_k, (int)pow(10, i), 10, (int)pow(k, i), (int)a_k / (int)pow(10, i) % 10 * (int)pow(k, i));
        a += (int)a_k / (int)pow(10, i) % 10 * pow(k, i);
    }
    for(i=0; pow(10, i)<=b_k; i++){
        // printf("b : %lf += %lf / %lf %% %lf * %lf = %lf\n", b, b_k, (int)pow(10, i), 10, (int)pow(k, i), (int)b_k / (int)pow(10, i) % 10 * (int)pow(k, i));
        b += (int)b_k / (int)pow(10, i) % 10 * pow(k, i);
    }
    // printf("%lf %lf\n", a, b);
    printf("%lf", a*b);
}