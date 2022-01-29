import math

N, L, W = (int(v) for v in input().split(' '))
a = [int(v) for v in input().split(' ')]

'''
1度目の諦め
# bridge = [False] * (L+1)
# for ai in a:
#     bridge[ai:ai+W+1] = [True] * (W+1)

# print(bridge)

# not_covered = [0]
# for i in range(len(bridge)):
#     if bridge[i] == False:
#         not_covered[-1] += 1
#     if i != 0 and bridge[i-1] == False and bridge[i] == True:
#         not_covered.append(0)
'''
'''
# not_covered = [0]
# i = 0
# for j in range(L+1) :
#     if j >= a[i] and j <= a[i]+W:
#         not_covered[-1] += 1
#     if j == a[i]+W:
#         not_covered.append(0)
#         i += 1
#         if i >= len(a):
#             break

# ans = 0
# for space in not_covered:
#     if space <= W and space != 0:
#         ans += 1
#     else:
#         ans += int(space/W)
'''

ans = 0
npos = 0
for ai in a:
    print('現在地:', npos, '\t次のシート:', ai, '~', ai+W)
    if npos < ai+W:
        ans += math.ceil((ai - npos)/W)
        npos = ai + W

print('現在地:', npos, '\t橋の端:', L)
ans += math.ceil((L - npos)/W)

print(ans)
