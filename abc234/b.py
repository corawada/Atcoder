import math
N = int(input())

zahyo = list()

max_len = 0
for _ in range(N):
    x, y = map(int, input().split())
    for z in zahyo:
        if (z[0]-x)**2 + (z[1]-y)**2 > max_len:
            max_len = (z[0]-x)**2 + (z[1]-y)**2
    zahyo.append([x, y])

print(math.sqrt(max_len))

