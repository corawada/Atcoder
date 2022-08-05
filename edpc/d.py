n, k = map(int, input().split())

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    w, v = map(int, input().split())
    for j in range(k+1):
        if j - w >= 0:
            dp[i][j] = max(dp[i-1][j-w] + v, dp[i][j-1], dp[i-1][j])
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[n][k])


