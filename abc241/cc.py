N = int(input())

nn = [list(input()) for _ in range(N)]

dx = [1, 1, 1, 0]
dy = [-1, 0, 1, 1]

def search_sharp(a, b):
    for sx, sy in zip(dx, dy):
        count = 1
        x = a
        y = b
        for k in range(5):
            x += sx
            y += sy

            if (y<0) or (y>=N) or (x>=N):
                if count <= 3:
                    break
                else:
                    nx = a - abs(k - 5)* sx
                    ny = b - abs(k - 5)* sy
                    if (ny<0) or (ny>=N) or (nx<0):
                        break
                    else:
                        return True


            if nn[x][y] == '#':
                count += 1
        else:
            if count >= 4:
                return True

    return False


flag = False
for i in range(N):
    for j in range(N):
        if nn[i][j] == '#':
            if search_sharp(i, j):
                flag = True
        if flag:
            break
    if flag:
        break


if flag:
    print('Yes')
else:
    print('No')


