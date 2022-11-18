x, y, z = map(int, input().split())

if x < 0:
    x = -x
    y = -y
    z = -z

if x < y:
    print(x)
else:
    if y < 0:
        print(x)
    elif z < 0:
        print(2 * (-z) + x)
    elif z < y:
        print(x)
    else:
        print(-1)


