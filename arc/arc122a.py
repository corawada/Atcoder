n = int(input())
A = list(map(int, input().split()))
mod = 10 ** 9 + 7

dp = [[0, 0] for _ in range(n)]

dp[0][0] = 1

for i in range(n-1):
    dp[i+1][0] = (dp[i][0] + dp[i][1]) % mod
    dp[i+1][1] = (dp[i][0]) % mod

dps = [[0, 0] for _ in range(n)]
dps[0][0] = A[0]
for i, c in enumerate(dp[1:]):
    dps[i+1][0] = (dps[i][0] + dps[i][1] + dp[i+1][0] * A[i+1]) % mod
    dps[i+1][1] = (dps[i][0] - dp[i+1][1] * A[i+1]) % mod

print(sum(dps[-1]) % mod)

