h, w = map(int, input().split())
table = list()
for _ in range(h):
    table.append(input())

now = [0, 0]

already = set()
while True:
    nex = table[now[0]][now[1]]

    next_p = now.copy()
    if nex == 'U':
        next_p[0] -= 1
    elif nex == 'D':
        next_p[0] += 1
    elif nex == 'L':
        next_p[1] -= 1
    elif nex == 'R':
        next_p[1] += 1

    if (0<=next_p[0]<=h-1) and (0<=next_p[1]<=w-1):
        if (now[0]*w) + now[1] in already:
            print(-1)
            break
        else:
            already.add(now[0]*w + now[1])
            now = next_p

    else:
        print(now[0] + 1, now[1] + 1)
        break


