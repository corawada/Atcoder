from pprint import pprint

N, M, K = map(int, input().split())

dp = [[0]*(K+1) for _ in range(N+1)]
pprint(dp)

for s in range(1, M+1):
    dp[1][s] = 1
pprint(dp)

for k in range(2, N+1):
    for s in range(2, K+1):
        dp[k][s] = sum(dp[k-1][max(0,s-M):s])
        dp[k][s] %= 998244353
pprint(dp)


print (sum(dp[N]) % 998244353)
