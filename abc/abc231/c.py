from collections import deque

N, Q = map(int, input().split())

A = sorted(deque(map(int, input().split())))

def binary_search(x):
    l = 0
    r = N
    while r - 1 >= 1:
        i = (l + r) // 2
        if i == N -1:
            if A[i] >= x:
                return 1
            else:
                return 0
        if (A[i] < x) and (A[i+1] < x):
            l = i + 1
        elif (A[i] >= x) and (A[i+1] >= x):
            r = i
        elif (A[i] < x) and (A[i+1] >= x):
            return N - i - 1
    else:
        if A[0] >= x:
            return N
        else:
            return N - 1

for _ in range(Q):
    print(binary_search(int(input())))






    
