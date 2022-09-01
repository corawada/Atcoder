n = int(input())
T = list(map(int, input().split()))

sum_t = sum(T)

dp = [[False]*(sum_t+1) for _ in range(n+1)]
dp[0][0] = True

for idx, a in enumerate(T):
    dp[idx+1] = dp[idx].copy()
    
    for value, column in enumerate(dp[idx]):
        if column:
            dp[idx+1][value+a] = True

for idx, pre_ans in enumerate(dp[n][(sum_t+1)//2:]):
    if pre_ans:
        print((sum_t+1)//2 + idx)
        break
