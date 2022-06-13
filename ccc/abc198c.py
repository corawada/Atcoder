import math
k, x, y = map(int, input().split())

kyo = math.sqrt(x**2 + y**2) / k


print(math.ceil(kyo) if kyo >= 1 else 2)
