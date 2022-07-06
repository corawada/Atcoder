n, m = map(int, input().split())
A = set([int(input()) for _ in range(m)])
mod = (10**9) + 7

dp = [0] * (n+1)
dp[0] = 1
if 1 in A:
    dp[1] = 0
else:
    dp[1] = 1

for step in range(2, n+1):
    if step in A:
        continue
    else:
        dp[step] = (dp[step-1] + dp[step-2]) % mod

print(dp[n] % mod)


