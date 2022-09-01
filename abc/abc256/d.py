n = int(input())

A = [0] * (2 * 10**5 + 1)

for _ in range(n):
    a, b = map(int, input().split())
    A[a] += 1
    A[b] -= 1

for i in range(len(A)):
    if i > 0:
        A[i] += A[i-1]
    if (A[i-1] == 0) and (A[i] > 0 ):
        s = i
    elif (A[i-1] > 0) and (A[i] == 0):
        e = i
        print(s, e)

