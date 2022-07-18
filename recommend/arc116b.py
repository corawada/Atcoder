n = int(input())
A = sorted(list(map(int, input().split())))
mod = 998244353

B = A[n-1]
ans = pow(A.pop() ,2 ,mod)

for _ in range(n-1):
    a = A.pop()
    ans += pow(a, 2, mod)
    ans += (a * B) % mod
    B = (2*B + a)%mod

print(ans%mod)

