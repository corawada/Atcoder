h, w = map(int, input().split())
nn = list()

for _ in range(h):
    nn.append(input())

# print(nn)

def dfs(y, x, depth):
    # print("call dfs y: {} x: {} , depth:{}".format(y, x, depth))
    if (y==h) or (x==w):
        return depth - 1
    elif nn[y][x] == '#':
        return depth - 1
    else:
        return max(dfs(y+1, x, depth+1), dfs(y, x+1, depth+1))

print(dfs(0, 0, 1))


