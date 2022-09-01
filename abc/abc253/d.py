n, a, b = map(int, input().split())
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd (a, b)

ans = (1+n)*n//2


aa = n // a
bb = n // b
ab = n // lcm(a, b)

ans -= (((1+aa)*aa)//2)*a
ans -= (((1+bb)*bb)//2)*b

ans += (((1+ab)*ab)//2)*(lcm(a, b))

print(ans)

