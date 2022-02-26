N = int(input())
S = []
for i in range(N):
    S.append(input())

ST = []
for i in range(N):
    tmp = ''
    for j in range(N):
        tmp += S[j][i]
    ST.append(tmp)

# print(S)
# print(ST)

for i in range(N):
    for j in range(N-5):
        if list(S[i][j:j+6]).count('#') >= 4:
            print('Yes')
            exit()
        if list(ST[i][j:j+6]).count('#') >= 4:
            print('Yes')
            exit()

diagS = [S[i][i] for i in range(N)]
diagSF = [S[N-i-1][i] for i in range(N)]

if len(diagS) >= 6 and list(diagS).count('#') == len(diagS):
    print('Yes')
    exit()
if len(diagSF) >= 6 and list(diagSF).count('#') == len(diagSF):
    print('Yes')
    exit()

print('No')