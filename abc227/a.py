n, k, a = map(int, input().split())

fact_k = k % n + a - 1


if fact_k == 0:
    print(n)
elif fact_k <= n:
    print(fact_k)
else:
    print(fact_k - n)




