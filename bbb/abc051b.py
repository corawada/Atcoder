k, s = map(int, input().split())

count = 0
for x in range(0, k+1):
    for y in range(0, k+1):
        z = s - x -y
        if 0 <= z <= k:
            count += 1

print(count)
