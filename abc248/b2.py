from math import log, ceil

a, b, k = map(int, input().split())

ans = 0
while a * k**ans < b:
    ans += 1

print(ans)
