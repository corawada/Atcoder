n, m, k = map(int, input().split())
mod = 998244353

masu = {i:0 for i in range(n)}
masu_n = 0

masu[0] = m ** k

for _ in range(k):
    next_masu = {i:0 for i in range(n)}
    for key, value in masu.items():
        hitotu = value // m
        if hitotu == 0:
            continue

        for step in range(1, m+1):
            if key + step < n:
                next_masu[key+step] += hitotu
            elif key + step == n:
                masu_n += hitotu
            else:
                next_masu[2*n-key-step] += hitotu

    masu = next_masu.copy()

print(masu_n)


print(pow(2, 1, mod))
