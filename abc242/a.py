a, b, c, x = map(int, input().split())

if x <= b:
    if x <= a:
        print(1)
    else:
        print(c/(b-a))
else:
    print(0)
