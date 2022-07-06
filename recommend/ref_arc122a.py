MOD=10**9+7
N=int(input())
A=list(map(int,input().split()))
dp=[[0,0]for i in range(N)]
dp[0][0]=1
dp[0][1]=0

for i in range(N-1):
    dp[i+1][0]=(dp[i][0]+dp[i][1])%MOD
    dp[i+1][1]=(dp[i][0])%MOD
ans=A[0]*(dp[N-1][0]+dp[N-1][1])%MOD

for i in range(1,N):
    ans+=A[i]*dp[i][0]*dp[N-i][0]
    ans-=A[i]*dp[i][1]*dp[N-i][1]
    ans%=MOD
print(ans)
print(dp)
