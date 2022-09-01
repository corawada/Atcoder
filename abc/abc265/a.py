x, y, n = map(int, input().split())

if 3*x <= y:
    print(n*x)
else:
    print((n//3)*y + (n%3)*x)

