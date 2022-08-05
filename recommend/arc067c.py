n = int(input())

A = list(map(int, input().split()))

sum_a = sum(A)
rui = 0
ans = 10 ** 10
for a in A[:-1]:
    rui += a
    ans = min(ans, abs(sum_a-2*rui))

print(ans)
