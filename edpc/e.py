n, k = map(int, input().split())

# dp = [[10**10]*(10**5+1) for _ in range(n+1)]
dp = [dict() for _ in range(n+1)]
dp[0] = {0:0}

for i in range(1, n+1):
    w, v = map(int, input().split())

    dp[i] = dp[i-1].copy()
    dp_keys = list(dp[i-1].keys()).copy()
    for j in dp_keys:
        if j+v in dp[i].keys():
            dp[i][j+v] = min(dp[i][j+v], dp[i][j] + w)
        else:
            dp[i].update({j+v:dp[i][j] + w})


ans = 0
for key, value in dp[n].items():
    if value <= k:
        ans = max(ans, key)

print(ans)
print(dp[n][ans])





