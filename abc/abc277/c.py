n = int(input())

ladders = list()

for _ in range(n):
    a, b = map(int, input().split())
    ladders.append([a, b])

able = {1}
ladders = sorted(ladders, reverse=True)

# 階段を下に降りることも考慮しなければならない

max_b = 1
while ladders:
    lad = ladders.pop()
    if lad[0] in able:
        able.add(lad[1])
        max_b = max(max_b, lad[1])

print(max_b)



