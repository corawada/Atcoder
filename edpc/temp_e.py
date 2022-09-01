n, k = map(int, input().split())

dp = [dict() for _ in range(n+1)]
dp[0] = {0:0}

for i in range(1, n+1):
    w, v = map(int, input().split())

    dp[i] = dp[i-1].copy()
    dp_keys = list(dp[i-1].keys()).copy()
    for j in dp_keys:
        if j+v in dp[i].keys():
            dp[i][j+v] = min(dp[i][j+v], dp[i-1][j] + w)
        else:
            dp[i].update({j+v:dp[i][j] + w})


ans = 0
for key, weight in dp[n].items():
    if weight <= k:
        ans = max(ans, key)

print(ans)





