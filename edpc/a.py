n = int(input())
A = list(map(int, input().split()))


dp = [0] * (n+1)
dp[1] = 0
dp[2] = abs(A[1] - A[0])


for i in range(3, n+1):
    dp[i] = min(dp[i-2] + abs(A[i-3] - A[i-1]), dp[i-1] + abs(A[i-2] - A[i-1]))

print(dp[n])
