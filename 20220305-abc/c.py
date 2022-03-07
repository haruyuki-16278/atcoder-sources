N = int(input())

cnt = 0
for X in range(int('1'*(N)), (10**(N))):
    breaked = False
    sX = str(X)
    if '0' in set(sX):
        continue
    for i in range(N-1):
        if abs(int(sX[i])-int(sX[i+1])) > 1:
            breaked = True
            break
    if breaked:
        continue
    cnt += 1

print(cnt % 998244353)