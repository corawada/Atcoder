n = int(input())

A = list(map(int, input().split()))


for idx, i in enumerate(A[:-2]):
    for idx2, j in enumerate(A[idx+1:-1]):
        if i < j
