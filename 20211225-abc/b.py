L, R = (int(v) for v in input().split(' '))
S = input()

fixed_L = S[0:L-1]
reverse = S[L-1:R][::-1]
fixed_R = S[R:]

print(fixed_L+reverse+fixed_R)
