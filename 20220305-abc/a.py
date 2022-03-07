A, B, C, X = (int(v) for v in input().split(' '))

if X <= A:
    print('1')
    exit()

if X > B:
    print('0')
    exit()

if X > A and X <= B:
    p = C / (B - A)
    print(p)
    exit()
