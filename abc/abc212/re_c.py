from bisect import bisect
n, m = map(int, input().split())

A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

ans = 10**10
for a in A:
    k = bisect(B, a)
    try:
        ans = min(ans, abs(a-B[k]))
    except:
        pass

    try:
        ans = min(ans, abs(a-B[k-1]))
    except:
        pass

print(ans)

