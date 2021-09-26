n = input()
a = input().split(' ')
a = [int(an) for an in a]

cnt = 0
flag = True
while flag:
    for i in range(len(a)):
        if a[i]%2 == 1:
            flag = False
        a[i] = int(a[i] / 2)
    cnt += int(flag)
print(cnt)
