from bisect import bisect_right

n, k = map(int, input().split())
A = list(map(int, input().split()))
a_zero = bisect_right(A, 0)

a_min = [0]
a_plu = [0]
a_min.extend([-i for i in A[:a_zero][::-1]])
a_plu.extend(A[a_zero:])

ans = 10**10
for i in range(k+1):
    try:
        m = a_min[i] * 2 + a_plu[k-i]
        ans = min(ans, m)
    except:
        pass

    try:
        m = a_min[i] + a_plu[k-i] * 2
        ans = min(ans, m)
    except:
        pass

print(ans)
