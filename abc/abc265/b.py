n, m, t = map(int, input().split())
A = list(map(int, input().split()))
bonas = dict()
for _ in range(m):
    x, y = map(int, input().split())
    bonas[x-2] = y

for idx, a in enumerate(A):
    t -= a
    if t <= 0:
        print('No')
        break
    if idx in bonas:
        t += bonas[idx]
else:
    print('Yes')

