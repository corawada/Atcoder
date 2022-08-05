n = int(input())

A = list(map(int, input().split()))
MOD = 998244353

ans = 0
for t in range(1, n+1):
    dp = [[[False]*t for _ in range(n+1)] for _ in range(n+1)]
    dp[0][0][0] = 1
    
    for i in range(1, n+1):
        a_mo = A[i-1] % t
        for j in range(i+1):
            for k in range(t):
                m = (k+a_mo) % t
                # 別のdpに遷移
                if j != t + 1:
                    dp[i][j][m] += dp[i-1][j-1][k] % MOD

                # そのaを選ばない時
                dp[i][j][k] += dp[i-1][j][k] 

    ans += dp[n][t][0] % MOD
    ans %= MOD

print(ans)




