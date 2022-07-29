n = int(input())
A = list(map(int, input().split()))

mod = (10**9) + 7

dp = [[0, 0] for _ in range(n)]
dp[0] = [1, 0]
dp[1] = [1, 1]

for i in range(2, n):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]

dp_sum = sum(dp[n-1])
ans = 0
pre_0, pre_1 = dp_sum, 0
for a, hi in zip(A[::-1],dp[::-1]):
    plu = int(pre_0*(hi[0]/sum(hi)) + pre_1)
    mia = dp_sum - plu
    pre_0, pre_1 = plu, mia
    ans += a * (plu - mia)
    print(a, plu, mia, hi)

print(ans%mod)


