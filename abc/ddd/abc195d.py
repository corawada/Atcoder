n, m, Q = map(int, input().split())

load = list()
for _ in range(n):
    load.append(list(map(int, input().split())))

load = sorted(load, key=lambda x:x[1])
print(load)
X = list(map(int, input().split()))
print()

for _ in range(Q):
    l, r = map(int, input().split())
    box = X[:l-1] + X[r:]
    print(box)
