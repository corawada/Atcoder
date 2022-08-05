n = int(input())


pre_a, pre_b, pre_c = 0, 0, 0


for i in range(1, n+1):
    a, b, c = map(int, input().split())

    now_a = max(pre_b + a, pre_c + a)
    now_b = max(pre_a + b, pre_c + b)
    now_c = max(pre_a + c, pre_b + c)

    pre_a, pre_b, pre_c = now_a, now_b, now_c


print(max(now_a, now_b, now_c))

