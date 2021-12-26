N, X = (int(v) for v in input().split(' '))

L = []
a = []
for i in range(N):
    rec = [int(v) for v in input().split(' ')]
    L.append(rec[0])
    a.append(rec[1:])

print(N, X, L, a)

for i in range(N):
    for j in range(L[i]):
        print(i, j)
