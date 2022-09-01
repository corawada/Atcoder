n = int(input())
A = list(map(int, input().split()))
mod = 998244353

pre = [0]*10
pre[A[0]] = 1
now = [0]*10

for idx, a in enumerate(A[1:]):
    now = [0]*10
    for pre_num, value  in enumerate(pre):
        now[(pre_num+a)%10] += value % mod
        now[(pre_num*a)%10] += value % mod
    pre = now


for ans in now:
    print(ans%mod)
