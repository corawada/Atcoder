n = int(input())

dai = list()

for _ in range(n):
    x, y, p = map(int, input().split())
    dai.append([x, y, p])

print(dai)
