h, w = map(int, input().split())

nn = list()

for _ in range(h):
    nn.append(input())

ans = [0] * w
for row in nn:
    for j in range(w):
        if row[j] == '#':
            ans[j] += 1

print(' '.join([str(a) for a in ans]))

