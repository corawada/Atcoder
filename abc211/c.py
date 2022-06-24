import re
S = input()
T = 'chokudai'

dp = [[1]+[0]*(len(T)) for _ in range(len(S) + 1)]

for s in range(len(S)):
    for t in range(len(T)):
        if S[s] == T[t]:
            dp[s+1][t+1] = (dp[s][t] + dp[s][t+1]) % (10**9 + 7)
        else:
            dp[s+1][t+1] = (dp[s][t+1]) % (10**9 + 7)

print(dp[s+1][t+1])




