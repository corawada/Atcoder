x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

new_x = x2 - x1
new_y = y2 - y1

ans = 3

for u in range(-3, 4):
    for m in range(-3, 4):
        if abs(u) + abs(m) <= 3:
            if (new_x - u) == (new_y - m):
                ans = 2
            if abs(new_x - u) + (new_y- m) <= 3:
                ans = 2

if (new_x + new_y) % 2 == 0:
    ans = 2

if (new_x) == (new_y):
    ans = 1
elif abs(new_x) + abs(new_y) <= 3:
    ans = 1

if (new_x == 0) and (new_y == 0):
    ans = 0

print(ans)

