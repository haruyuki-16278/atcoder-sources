from math import sqrt

x1, y1, x2, y2 = (int(v) for v in input().split(' '))

points_1 = [
    (x1+2, y1+1),
    (x1+1, y1+2),
    (x1-1, y1+2),
    (x1-2, y1+1),
    (x1-2, y1-1),
    (x1-1, y1-2),
    (x1+1, y1-2),
    (x1+2, y1-1)
]

points_2 = [
    (x2+2, y2+1),
    (x2+1, y2+2),
    (x2-1, y2+2),
    (x2-2, y2+1),
    (x2-2, y2-1),
    (x2-1, y2-2),
    (x2+1, y2-2),
    (x2+2, y2-1)
]

for point_1 in points_1:
    if point_1 in points_2:
        print('Yes')
        exit()

print('No')