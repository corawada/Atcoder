n, a, b = map(int, input().split())

sum_n = 0
for i in range(1, n+1):
    str_n = str(i)
    value = 0
    for j in str_n:
        value += int(j)
    if (a <= value) and (value <= b):
        sum_n += i
print(sum_n)

