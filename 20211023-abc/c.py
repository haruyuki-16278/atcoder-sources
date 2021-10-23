N = int(input())
XY = []
for i in range(N):
    XY.append([int(x) for x in input().split(' ')])

x = 0
y = 1

cnt = 0
for i in range(N):
    for j in range(i, N):
        for k in range(j, N):
            if (0.5 * ((XY[j][x] - XY[i][x])*(XY[k][y] - XY[i][y]) - (XY[k][x] - XY[i][x])*(XY[j][y] - XY[i][y])) != 0):
                cnt += 1

print(cnt)