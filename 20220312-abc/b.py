N = int(input())
A = [int(v) for v in input().split(' ')]
B = [int(v) for v in input().split(' ')]

sB = set(B)

same = 0
included = 0

for i in range(N):
    if A[i] == B[i]:
        same += 1
    elif A[i] in sB:
        included += 1

print(same)
print(included)