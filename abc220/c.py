n = int(input())
A = list(map(int, input().split()))
k = int(input())

sum_a = sum(A)

s = k // sum_a
amari = k % sum_a

for i,a in enumerate(A):
    if amari >= 0:
        amari -= a
    else:
        print(s*n+i)
        break
else:
    print(n*(s+1))
