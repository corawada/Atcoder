# from pprint import pprint
S = input()
T = input()

dp = [[0]*(len(T)+1) for _ in range(len(S)+1)]


for i in range(len(S)):
    for j in range(len(T)):
        if S[i] == T[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

# pprint(dp)
ans = ""

now_i = len(S) 
now_j = len(T) 
tar = dp[len(S)][len(T)]

ans = ""
while tar != 0:
    if S[now_i-1] == T[now_j-1]:
        ans += S[now_i-1]
        tar -= 1
        now_i -= 1
        now_j -= 1
    else:
        if dp[now_i-1][now_j] > dp[now_i][now_j-1]:
            now_i -= 1
        else:
            now_j -= 1

print(ans[::-1])


