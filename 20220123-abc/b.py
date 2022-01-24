N = int(input())
A = [int(v) for v in input().split(' ')]

cnt = [0] * (N+1)
for a in A:
    cnt[a] += 1

index = cnt.index(3)
print(index)