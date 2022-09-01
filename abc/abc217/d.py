import bisect
import array
l, q = map(int, input().split())

div_point = array.array('i', [0, l])

for _ in range(q):
    x, k = map(int, input().split())
    y = bisect.bisect(div_point, k)
    if x == 1:
        div_point.insert(y, k)
    else:
        print(div_point[y] - div_point[y-1])
