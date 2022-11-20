from collections import defaultdict

n, q = map(int, input().split())

friend = defaultdict(set)

for _ in range(q):
    t, a, b = map(int, input().split())

    if t == 1:
        friend[a].add(b)
    elif t == 2:
        friend[a].discard(b)
    elif t == 3:
        if (b in friend[a]) and (a in friend[b]):
            print('Yes')
        else:
            print('No')

