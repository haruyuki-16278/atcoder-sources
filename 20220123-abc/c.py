N, M = (int(v) for v in input().split(' '))
S = input().split(' ')
T = input().split(' ')

ans = {sta: 'No' for sta in S}
for ti in T:
    ans[ti] = 'Yes'

for k, v in ans.items():
    print(v)