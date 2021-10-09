#include <stdio.h>

int main(void) {
    // ループ用
    int i, j, k;

    // 入力受け取り
    int n, m;
    scanf("%d %d", &n, &m);
    char a_tmp[2*n][m];
    for(i=0; i<2*n; i++){
        scanf("%s", a_tmp[i]);
    }
    char a[2*n][m];
    // 文字列パース
    for(i=0; i<2*n; i++){
        for(j=0; j<m; j++){
            a[i][j] = (char)a_tmp[i][j];
        }
    }

    // 処理
    int win[2*n], rank[2*n];
    int cnt;
    for(i=0; i<2*n; i++){
        win[i] = 0;
        rank[i] = i;
    }
    for(i=0; i<m; i++){
        // 勝数カウント
        for(j=0; j<2*n; j+=2){
            if(
                (a[rank[j]][i] == 'G' && a[rank[j+1]][i] == 'C') ||
                (a[rank[j]][i] == 'C' && a[rank[j+1]][i] == 'P') ||
                (a[rank[j]][i] == 'P' && a[rank[j+1]][i] == 'G')
            ) {
                win[rank[j]] += 1;
            }
            else if (
                (a[rank[j]][i] == 'P' && a[rank[j+1]][i] == 'C') ||
                (a[rank[j]][i] == 'G' && a[rank[j+1]][i] == 'P') ||
                (a[rank[j]][i] == 'C' && a[rank[j+1]][i] == 'G')
            ) {
                win[rank[j+1]] += 1;
            }
        }
        // 順位確定
        cnt = 0;
        for(k=m; k>=0; k--){
            for(j=0; j<n*2; j++){
                if(win[j] == k){
                    rank[cnt] = j;
                    cnt++;
                }
            }
        }
    }

    for(i=0; i<2*n; i++) {
        printf("%d\n", rank[i]+1);
    }

    return 0;
}