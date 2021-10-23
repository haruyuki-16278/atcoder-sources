H, W = [int(x) for x in input().split(' ')]
A = []
for i in range(H):
    A.append([int(x) for x in input().split(' ')])

H_comb = [list(range(i, H)) for i in range(H)][:-1]
W_comb = [list(range(i, W)) for i in range(W)][:-1]

flag = True

for x in H_comb:
    i1 = x[0]
    for i2 in x[1:]:
        for y in W_comb:
            j1 = y[0]
            for j2 in y[1:]:
                if A[i1][j1] + A[i2][j2] > A[i1][j2] + A[i2][j1]:
                    flag = False

print('Yes' if flag else 'No')
