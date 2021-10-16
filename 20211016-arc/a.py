N = int(input())
A = [int(a) for a in input().split(" ")]

print(max(A))
sortedA = sorted(A)
exchange_timing = []
cnt_g2s = 0
cnt_s2g = 0

for i, Ai in enumerate(A):
    
