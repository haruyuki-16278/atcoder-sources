#include <stdio.h>
#include <string.h>

int main(void) {
    // forループ用変数
    int i=0, j=0, k=0;

    // 入力受け取り処理
    int N, K, B;
    scanf("%d %d %d", &N, &K, &B);
    printf("N:%d K:%d B:%d\n", N, K, B);
    int x[K], y[K];
    for (i=0; i<K; i++) {
        scanf("%d %d", &x[i], &y[i]);
    }
    for (i=0; i<K; i++) {
        printf("mark%d : (%d,%d)\n", i, x[i], y[i]);
    }
    int n[B], m[B], C[B];
    int s[B][N][N];
    char* s_tmp;
    for (i=0; i<B; i++) {
        s_tmp="";
        scanf("%d %d %d", &n[i], &m[i], &C[i]);
        printf("サイズ:(%d,%d) コスト:%d\n", n[i], m[i], C[i]);
        for(j=0; j<m[i]; j++) {
            scanf("%s", s_tmp);
            printf("input:%s", s_tmp);
            for(k=0; k<n[i]; k++) {
                s[i][j][k] = (char)s_tmp[k];
            }
        }
    }
    for (i=0; i<B; i++) {
        for (j=0; j<n[i]; j++) {
            for (k=0; k<m[i]; k++) {
                if (s[i][j][k] == '#') {
                    printf("■");
                }
                else if (s[i][j][k] == ".") {
                    printf("□");
                }
            }
        }
    }

    // 入力結果確認

    // メイン処理
    

    return 0;
}