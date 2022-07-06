h, w = map(int, input().split())

S = ['.'*(w+2), ]

for _ in range(h):
    S.append('.'+ input()+'.')

S.append('.'*(w+2))

"""
for s in S:
    print(s)
"""

flag = True
for i in range(1, h+1):
    for j in range(1, w+1):
        if (i==1) and (j==1):
            if (S[i+1][j] + S[i][j+1]).count('#') != 1:
                flag = False
        elif (i==h) and (j==w):
            if (S[i-1][j] + S[i][j-1]).count('#') != 1:
                flag = False
        elif S[i][j] == '#':
            if (S[i-1][j] + S[i][j-1]).count('#') != 1:
                flag = False
            if (S[i+1][j] + S[i][j+1]).count('#') != 1:
                flag = False
        else:
            continue

print('Possible' if flag else 'Impossible')
