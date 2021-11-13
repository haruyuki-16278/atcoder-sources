import math

N = int(input())

correct = 0

# for a in range(1, int(math.pow(N, 1/3)+1)):
#     for b in range(a, int((math.sqrt(N)+1)/a)):
#         for c in range(b, int(N+1/a/b)):
#             print(a, b, c, a*b*c)
#             if a*b*c <= N:
#                 correct += 1

for a in range(1, int(math.pow(N, 1/3)+1)):
    for b in range(a, int((math.sqrt(N)+1)/a)):
        correct += N/(a*b)

print(correct)
