from bisect import bisect_right

n = int(input())
A = sorted(list(map(int, input().split())))
A.append(10**10)

q = int(input())

for _ in range(q):
    tar = int(input())
    i = bisect_right(A, tar)
    if i == 0:
        print(A[0] - tar)
    else:
        print(min(abs(A[i] - tar), abs(A[i-1] - tar)))


    

