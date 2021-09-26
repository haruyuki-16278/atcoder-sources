k = int(input())
ab_k = input().split(' ')
a_k = ab_k[0]
b_k = ab_k[1]

a=0
b=0

cnt = 0
for x in a_k[::-1]:
    a += int(x)*k**cnt
    cnt += 1

cnt  = 0
for x in b_k[::-1]:
    b += int(x)*k**cnt
    cnt += 1

print(a*b)