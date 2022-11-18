from collections import defaultdict

n, m = map(int, input().split())
A = sorted(list(map(int, input().split())))

k = [A[0], ]
for i in range(n-1):
    if A[i+1] - A[i] <= 1:
        k[-1] += A[i+1]
    else:
        k.append(A[i+1])

if (A[0] == 0) and (A[-1] == m-1) and (len(k) != 1):
    k[-1] += k[0]

print(sum(A) - max(k))




