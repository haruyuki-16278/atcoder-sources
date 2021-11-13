N, K, A = [int(x) for x in input().split(' ')]
if N == 1:
    print(1)
    exit()
l = [*range(A, N+1)] + [*range(1, N+1)] * int(K/N+1)
print(l[K-1])