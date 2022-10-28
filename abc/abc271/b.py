n, q = map(int, input().split())

nn = list()
for _ in range(n):
    nn.append(list(map(int, input().split()))[1:])

for _ in range(q):
    i, j = map(int, input().split())
    print(nn[i-1][j-1])

