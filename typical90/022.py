def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)

a, b, c = map(int, input().split())

saikoro = gcd(a, gcd(b, c))

print(a//saikoro + b//saikoro + c//saikoro - 3)
