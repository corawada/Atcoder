n = int(input())
A = list(map(int, input().split()))
mod = 10**9 + 7

rui = [0, ]

ans = 0
for a in A:
    ans += rui[-1]*a
    ans %= mod
    rui.append(rui[-1] + a)

print(ans)
