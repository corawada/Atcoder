n, m = map(int, input().split())

cond = list()
for _ in range(m):
    a, b = map(int, input().split())
    cond.append((a, b))

k = int(input())
choice = list()
for _ in range(k):
    c, d = map(int, input().split())
    choice.append((c, d))

ans = 0
for i in range(2**k):
    num = "{fil:0{le}b}".format(fil=i, le=k)
    sara = set()
    for idx,s in enumerate(num):
        sara.add(choice[idx][int(s)])

    tmp = 0
    for c in cond:
        if (c[0] in sara) and (c[1] in sara):
            tmp += 1

    ans = max(ans, tmp)

print(ans)


