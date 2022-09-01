from bisect import bisect_left

# import sys
# sys.setrecursionlimit(100000)
nCr = {}
def cmb(n, r):
    if r == 0 or r == n: return 1
    if r == 1: return n
    if (n,r) in nCr: return nCr[(n,r)]
    nCr[(n,r)] = cmb(n-1,r) + cmb(n-1,r-1)
    return nCr[(n,r)]


n = int(input())
A = list(map(int, input().split()))
A.append(0)
A = sorted(A)


las = A.pop()
tar = las // 2
A.append(las + 1)
tar_idx = bisect_left(A, tar)

if abs(tar - A[tar_idx]) > abs(tar - A[tar_idx-1]):
    print(las, A[tar_idx-1])
else:
    print(las, A[tar_idx])



