n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
mod = 998244353

dp = [[0]*3001 for _ in range(n+1)]

for j in range(A[0], B[0]+1):
    dp[1][j] = 1

for i in range(2, n+1):
    tmp = 0
    for k in range(0, A[i-1]):
        tmp += dp[i-1][k]
    for j in range(A[i-1], B[i-1] + 1):
        tmp += dp[i-1][j]
        tmp %= mod
        dp[i][j] = tmp

ans = sum(dp[n])
print(ans%mod)


