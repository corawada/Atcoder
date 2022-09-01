from math import sqrt
n, k = map(int, input().split())
A = set(map(int, input().split()))
lump = list()
non_lump = list()

for i in range(1, n+1):
    x, y = map(int, input().split())

    if i in A:
        lump.append([x, y])
    else:
        non_lump.append([x, y])

max_distance = 0
for h_x, h_y in non_lump:
    max_distance_ = 10**100
    for l_x, l_y in lump:
        dis = ((h_x-l_x) ** 2) + ((h_y-l_y) ** 2)
        max_distance_ = min(max_distance_, dis)
    max_distance = max(max_distance_, max_distance)

print(sqrt(max_distance))




