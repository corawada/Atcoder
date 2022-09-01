n = int(input())

x_dic = dict()

points = list()
ans = 0
for _ in range(n):
    x, y = map(int, input().split())

    if x in x_dic:
        x_dic[x].add(y)
    else:
        x_dic[x] = {y}

    for a, b in points:
        if (x == a) or (y == b):
            continue
        if (b in x_dic[x]) and (y in x_dic[a]):
            ans += 1

    points.append([x, y])

print(ans)
