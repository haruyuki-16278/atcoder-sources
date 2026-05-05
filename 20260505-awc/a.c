#include <stdio.h>
#include <stdlib.h>

// n個のメニューでm日のトレーニングをこなす
// メニュー毎にスタミナがあり、1回k消費する
// m日間メニューが持つかどうかを確認して、Yes/Noを出力する

int main(void) {
    long i;
    long n, m, k;
    scanf("%ld %ld %ld", &n, &m, &k);
    long *a = malloc(n * sizeof(long));
    for (i = 0; i < n; i++) {
        scanf("%ld", &a[i]);
    }

    // printf("%6ld 個のメニューで %10ld 日間のトレーニング\n%10ld ずつスタミナが減る\n", n, m, k);
    // for (i = 0; i < n; i++) {
    //     printf("メニュー%2ld, スタミナ: %10ld\n", i, a[i]);
    // }
    // printf("\n");

    long days = 0;
    for (i = 0; i < n; i++) {
        days += a[i] / k;
        // printf("%ld, %ld\n", a[i] / k, days);
    }
    // printf("%ld", days);

    if (days >= m) {
        printf("Yes");
    } else {
        printf("No");
    }

    free(a);
    return 0;
}