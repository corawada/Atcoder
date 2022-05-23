import math
X, Y = map(int, input().split())

ret = max(0, math.ceil((Y-X)/10))

print(ret)

