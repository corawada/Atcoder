n = int(input())
A = list(map(int, input().split()))

a_min = 10 ** 10
flag = 0
sum_a = 0
for a in A:
    if a < 0: flag += 1
    a = abs(a)
    sum_a += a
    a_min = min(a_min, a)

if flag % 2 == 0 :
    print(sum_a)
else:
    print(sum_a - 2 * a_min)

