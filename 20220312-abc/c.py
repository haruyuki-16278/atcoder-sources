N = int(input())
pos = []
for _ in range(N):
    pos.append([int(v) for v in input().split(' ')])
S = input()

human = [{pos: {'x': pos[i][0], 'y': pos[i][2]}, 'd': s}
            for i, s
            in enumerate(list(S))
        ].sort(key=lambda x: x['pos']['y'], reverse=True)

setY = set([p[1] for p in pos])

for y in setY:
    inY = [h for h in human if h['pos']['y'] == y]
    if len(inY) == 1:
        continue
    trace = {min}
    for h in inY:
        i

