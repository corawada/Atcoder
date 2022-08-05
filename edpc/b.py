n, k = map(int, input().split())
A = list(map(int, input().split()))

dp = [10**10] * (n+1)
dp[1] = 0

for i in range(1, n+1):
    for step in range(1, k+1):
        if i + step == n+1:
            break
        dp[i+step] = min(dp[i+step], dp[i] + abs(A[i-1] - A[i+step-1]))

print(dp[n])
