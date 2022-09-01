n, k = map(int, input().split())
A = list(map(int, input().split()))

sort_a = sorted(A)

if k%n == 0:
    sarv = k//n
    for _ in range(n):
        print(sarv)
else:
    sarv = k//n
    ikiti = sort_a[k%n -1]
    for a in A:
        if a <= ikiti:
            print(sarv+1)
        else:
            print(sarv)
