N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))


B = [0]*(M+1)
for m in range(M+1):
    coe = C.pop() 
    hikuyatu = 0
    for i in range(m):
        if N-1-i < 0:
            break
        hikuyatu += A[N-1-i] * B[M-m+1+i]

    coe -= hikuyatu
    coe //= A[-1]

    B[M-m] = coe

print(' '.join([str(b) for b in B]))


    
