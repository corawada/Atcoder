from bisect import bisect_left, insort
n, k = map(int, input().split())
A = list(map(int, input().split()))

mod = (10**9)+7

tento = list()

sort_A = sorted(A)
tmp_A = list()
for a in A[::-1]:
    insort(tmp_A, a)
    tento.append([bisect_left(sort_A, a), bisect_left(tmp_A, a)])

ans = 0
for t in tento:
    """
    ans += (t[1] * k) % mod
    ans += (t[0] * (((k-1)*k)//2)) % mod
    """
    ans += t[1] * k
    ans += t[0] * (((k-1)*k)//2) 

print(ans%mod)
