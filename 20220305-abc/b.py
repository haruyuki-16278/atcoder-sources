import string

S = input()

thereis = {k: 0 for k in string.ascii_lowercase}
for c in S:
    thereis[c] += 1

print(''.join([k*v for k, v in thereis.items()]))