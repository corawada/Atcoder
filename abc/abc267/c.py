n, m = map(int, input().split())
A = list(map(int, input().split()))

init_sum = 0
for idx, a in enumerate(A[:m]):
    init_sum += (idx+1) * a

tmp_max = init_sum
imos = [0, ]
for a in A:
    imos.append(imos[-1]+a)

zure = list()

for idx in range(n-m):
    zure.append(-(imos[idx+m] - imos[idx])+m*A[idx+m])

for z in zure:
    init_sum += z
    tmp_max = max(tmp_max, init_sum)

print(tmp_max)

