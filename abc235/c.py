from collections import deque

N, Q = map(int, input().split())
a = list(map(int, input().split()))

ans = ""
for _ in range(Q):
    A = a.copy()
    X, K = map(int, input().split())
    if X in A:
        idx = -1
        for _ in range(K):
            if not (X in A[idx+1:]):
                ans += "-1\n"
                break
            else:
                idx = A.index(X, idx+1)
        else:
            ans += "{}\n".format(idx+1)
    else:
        ans += "-1\n"

print(ans)

