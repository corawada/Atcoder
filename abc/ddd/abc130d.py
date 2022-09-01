from bisect import bisect_right, bisect_left
n, k = map(int, input().split())
A = list(map(int, input().split()))

rui = [0, ]

for a in A:
    rui.append(rui[-1] + a)

ans = 0
for l, ele in enumerate(rui):
    ans += n + 1 -bisect_left(rui, ele+k)

print(ans)
