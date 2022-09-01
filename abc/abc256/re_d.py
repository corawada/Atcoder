n = int(input())
imos = [0]*(2*(10**5) + 1)

for _ in range(n):
    l, r = map(int, input().split())
    imos[l] += 1
    imos[r] -= 1

now = 0
for idx, im in enumerate(imos):
    now = now + imos[idx]
    imos[idx] = now 

pre = 0
for idx, value in enumerate(imos):
    if (pre == 0) and (value > 0):
        print(idx, end=' ')
    elif (pre > 0) and (value == 0):
        print(idx)

    pre = value


