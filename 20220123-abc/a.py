S = input()
a, b = (int(v) for v in input().split(' '))

ans = S[:a-1] + S[b-1] + S[a:b-1] + S[a-1] + S[b:]
print(ans)