# from pprint import pprint
n, m = map(int, input().split())

X = list(map(int, input().split()))
# print(X)

bonas = {1:0}
for _ in range(m):
    c, y = map(int, input().split())
    bonas[c] = y

dp = [[0]*(n+1) for _ in range(n+1)]
dp[1][1] = X[0] + bonas[1]

for i in range(2, n+1):
    for idx, pre in enumerate(dp[i-1]):
        dp[i][0] = max(dp[i][0], pre)
        if idx+1 == i+1:
            break
        if idx+1 in bonas:
            dp[i][idx+1] = pre + X[i-1] + bonas[idx+1]
        else:
            dp[i][idx+1] = pre + X[i-1] 

# pprint(dp)
print(max(dp[n]))
