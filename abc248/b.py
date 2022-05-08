from math import log, ceil

a, b, k = map(int, input().split())

print(ceil(log(b/a, k)))


