N = input()
H = [int(i) for i in input().split(' ')]

for i in range(len (H)):
    if i != len(H)-1 and H[i] < H[i+1]:
        continue
    else:
        print(H[i])
        break
