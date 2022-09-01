v, a, b, c = map(int, input().split())

sum_v = a + b + c

v = v % sum_v

if v - a < 0:
    print("F")
elif v - (a + b) < 0:
    print("M")
else:
    print("T")

