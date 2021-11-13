N = int(input())
S = [int(s) for s in input().split(' ')]

ac = []

for a in range(1, 150):
    for b in range(1, 150):
        s = 4*a*b + 3*a + 3*b
        if s <= 1000 and not s in ac:
            ac.append(s)

# ac.sort()
# print(ac)

wa = 0
for s in S:
    if not s in ac:
        wa += 1

print(wa)
