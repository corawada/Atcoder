from bisect import bisect_left
x, a, d, n = map(int, input().split())
last = a + d*(n-1)
ad = abs(d)

if (a <= x <= last) or (last <= x <= a):
    if d == 0:
        print(abs(a-x))
    else:
        print(min((x-a)%ad, ad-(x-a)%ad))
else:
    if abs(a-x) > abs(last-x):
        print(abs(last-x))
    else:
        print(abs(a-x))



