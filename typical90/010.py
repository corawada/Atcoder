n = int(input())

rui = [(0, 0),]
for _ in range(n):
    a, b = map(int, input().split())
    c1, c2 = rui[-1]
    if a == 1:
        rui.append((c1 + b, c2))
    else:
        rui.append((c1 , c2 + b))

q = int(input())
for _ in range(q):
    fr, to = map(int, input().split())
    fr1, fr2 = rui[fr-1]
    to1, to2 = rui[to]

    print(to1-fr1, to2-fr2)

