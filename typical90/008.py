n = int(input())
S = input()
T = 'atcoder'

dp = [[0]*(len(T)+1) for _ in range(len(S)+1)]
for i in range(n+1):
    dp[i][0] = 1

for id_s, s in enumerate(S):
    for id_t, t in enumerate(T):
        if s == t:
            dp[id_s+1][id_t+1] = dp[id_s][id_t] + dp[id_s][id_t+1]
        else:
            dp[id_s+1][id_t+1] = dp[id_s][id_t+1]

print(dp[n][len(T)]%(10**9+7))
