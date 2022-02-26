N, M = (int(v) for v in input().split(' '))
A = [int(v) for v in input().split(' ')]
B = [int(v) for v in input().split(' ')]

for Bi in B:
    if Bi not in A:
        print('No')
        exit()
    A.remove(Bi)

print('Yes')
