n, m = map(int, input().split())
A = list(map(int, input().split()))

dp = [[-10**20]*(m+1) for _ in range(n+1)]

for id_i, a in enumerate(A):
    i = id_i + 1
    for j in range(1, min(i+1, m+1)):
        if j == 1:
            dp[i][j] = max(dp[i-1][1], a)
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + j * a)

ans = dp[n][m]
for row in dp[m:]:
    ans = max(ans, row[m])

print(ans)


