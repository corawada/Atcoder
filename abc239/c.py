import math
x1, y1, x2, y2 = map(int, input().split())

# 片方の点は原点に、もう片方は(x, y)にある
x = abs(x2 - x1)
y = abs(y2 - y1)

xn = min(x, y)
yn = max(x, y)

def calc_length(x, y, point):
    # return bool
    return (x-point[0])**2 + (y-point[1])**2 == 5

serch_list = [[2,1], [1,2], [-1,2], [-2,1],
              [-2,-1], [-1,-2], [1,-2], [2,-1] ]

flag = False
if (x > 10) or (y > 10):
    print("No")
else:
    for i in serch_list:
        if calc_length(xn, yn, i):
            flag = True
        else:
            pass

    if flag:
        print("Yes")
    else:
        print("No")


    





