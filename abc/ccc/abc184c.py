x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

# 片方を原点にせってし直す
new_x = x2 - x1
new_y = y2 - y1
# print(new_x, new_y)


if (new_x == 0) and (new_y == 0):
    print(0)
elif abs(new_x) + abs(new_y) <= 3:
    print(1)
elif abs(new_x) == abs(new_y):
    print(1)
elif -3 <= abs(new_x) - abs(new_y) <= 3:
    print('koko')
    print(2)
elif (new_x + new_y) % 2 == 0:
    print(2)

# elif abs(new_x) + abs(new_y) % 2 == 0:
#     print(2)
else:
    print(3)
        

