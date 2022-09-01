from bisect import bisect_right
n, q = map(int, input().split())
A = sorted(list(map(int, input().split())))

rui = {0:0}
sum_a = 0
for idx, a in enumerate(A):
    rui[idx+1] = rui[idx] + a
    sum_a += a

for _ in range(q):
    k = int(input())
    iki = bisect_right(A, k)
    print(2*k*iki - 2*rui[iki] + sum_a - k*n)
    
