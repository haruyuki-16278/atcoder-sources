def boring(data, score):
    if len(data[0]) == 1:
        ans.append(score^data[0][0])
    else:
        for i, a in enumerate(data[0]):
            data.pop()
            data.pop(i)
            boring

N = int(input())
A = {}
for i in range(1, 2*N):
    A[str(i)] = {str(i+j+1): int(v) for j, v in enumerate(input().split(' '))}

print(A)
print(A['1'])
ans = []