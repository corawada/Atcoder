n, k = map(int, input().split())
data = list()
for _ in range(n):
    w, v = map(int, input().split())
    data.append([w, v])

# print(data)

dp = [[k+1]*(10**5+1) for _ in range(n+1)]
dp[0][0] = 0

touch_set = {0}
for idx, elem in enumerate(data):
    nex = set()
    for j in touch_set:
        dp[idx+1][j+elem[1]] = min(dp[idx+1][j+elem[1]], dp[idx][j] + elem[0])
        dp[idx+1][j] = min(dp[idx+1][j] , dp[idx][j])
        nex.add(j+elem[1])
    touch_set |= nex

ans = -1

for idx, weight in enumerate(reversed(dp[n])):
    if weight <= k:
        print(10**5 - idx)
        break




