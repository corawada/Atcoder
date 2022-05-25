H, W = map(int, input().split())

nn = [list(map(int, input().split())) for _ in range(H)]

flag = True
for i in range(H):
    for i2 in range(i+1, H):
        for j in range(W):
            for j2 in range(j+1, W):
                if nn[i][j] + nn[i2][j2] <= nn[i2][j] + nn[i][j2]:
                    pass
                else:
                    flag = False

if flag:
    print("Yes")
else:
    print("No")
