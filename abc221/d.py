from collections import defaultdict
n = int(input())

imos_d = defaultdict(int)
for _ in range(n):
    a, b = map(int, input().split())
    imos_d[a] += 1
    imos_d[a+b] -= 1

imos = sorted(list(imos_d.items()), reverse=True)

ans_d = defaultdict(int)
pre_num = 0
pre_value = 0
while imos:
    num, value = imos.pop()
    ans_d[pre_value] += num-pre_num
    pre_value += value
    pre_num = num

for i in range(1, n+1):
    print(ans_d[i], end=' ')
print()
