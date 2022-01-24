def borling(data, nowfloor, nowscore):
    if (len(data[nowfloor]) == 1):
        ans.append(nowscore^data[nowfloor+1][0])
    else:
        for i, a in enumerate(data[nowfloor]):
            data.pop()
            borling(data, nowfloor+1, nowfloor^a)

N = int(input())
A = []
for i in range(2*N-1):
    A.append([int(v) for v in input().split(' ')])

ans = []
borling(A, 0, 0)
print(ans)
print(max(ans))
