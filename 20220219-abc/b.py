X = input()

if X[-1] == '0':
    print(X[:-1] if X != '0' else 0)
else:
    if X[0] == '-':
        print('-' + str(int(X[1:-1]) + 1) if len(X) > 2 else '-1')
    else:
        print(X[:-1] if len(X) > 1 else '0')