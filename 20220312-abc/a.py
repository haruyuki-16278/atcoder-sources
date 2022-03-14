V, A, B, C = (int(v) for v in input().split(' '))

while (True):
    for who, use in {'F': A, 'M': B, 'T': C}.items():
        if V >= use:
            V -= use
        else:
            print(who)
            exit()