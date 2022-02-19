A, B, C, D = (int(v) for v in input().split(' '))

prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

table = {v:'Takahashi' for v in range(A, B+1)}

for takahashi in table.keys():
    for aoki in range(C, D+1):
        # print('takahashi:', takahashi, 'aoki:', aoki, 'sum is prime:', takahashi + aoki in prime_numbers)
        if takahashi + aoki in prime_numbers:
            table[takahashi] = 'Aoki'
            break

# print(table)

if 'Takahashi' in table.values():
    print('Takahashi')
else:
    print('Aoki')