a, b, c, d, e, f, x = map(int, input().split())

taka = (x//(a+c)) * a*b + min(a,x%(a+c))*b
aoki = (x//(d+f)) * d*e + min(d, x%(d+f))*e

if taka < aoki:
    print("Aoki")
elif taka > aoki:
    print("Takahashi")
else:
    print("Draw")
