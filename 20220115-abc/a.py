abc = input()
bca = abc[1:] + abc[0]
cab = bca[1:] + bca[0]
abc = int(abc)
bca = int(bca)
cab = int(cab)

print(abc + bca + cab)
