N = int(input())
XY = []
for i in range(N):
    XY.append([int(x) for x in input().split(' ')])

import itertools
x = 0
y = 1

tri_ps = itertools.combinations(XY, 3)

cnt = 0
for tri_p in tri_ps:
    g = (tri_p[0][y] - tri_p[1][y])/(tri_p[0][x] - tri_p[1][x]) if (tri_p[0][x] - tri_p[1][x]) != 0 else 0
    i = tri_p[0][y] - g*tri_p[0][x]
    if g*tri_p[2][x] + i - tri_p[2][y]:
        cnt += 1

print(cnt)