from math import sqrt

a, b = map(int, input().split())

tan = sqrt(a**2+b**2)
print("{} {}".format(a/tan, b/tan))

