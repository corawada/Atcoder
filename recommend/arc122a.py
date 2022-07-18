n = int(input())
A = list(map(int, input().split()))

mod = (10**9) + 7

dp = [[0, 0] for _ in range(n)]
dp[1] = [1, 1]

print(dp)

for i in range(2, n):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0] 

print(dp)

full = sum(dp[n-1])
print(full)
ans = 0
for i in range(n):


print(ans)
