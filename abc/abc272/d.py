from math import sqrt
n, m = map(int, input().split())

nn = [[-1]*n for _ in range(n)]
nn[0][0] = 0

directions = list()
for i in range(n+1):
    if m-i**2 >= 0:
        j = int(sqrt(m-i**2))
        if i**2 + j**2 == m:
            directions.append([i, j])
            directions.append([-j, i])
            directions.append([-i, -j])
            directions.append([j, -i])

## bfs の実装
stack = [[0, 0], ]
counter = 0
while stack:
    counter += 1
    pre_stack = list()
    for i, j in stack:
        for si, sj in directions:
            ai = i + si
            aj = j + sj
            if (0 <= ai <= n-1) and (0 <= aj <= n-1) and (nn[ai][aj] == -1):
                nn[ai][aj] = counter
                pre_stack.append([ai, aj])

    stack = pre_stack

nn[0][0] = 0

for raw in nn:
    for s in raw:
        print("{} ".format(s), end="")
    print()





