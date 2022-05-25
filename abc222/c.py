N, M = map(int, input().split())

A = [[0, input(), i] for i in range(2*N)]

for k in range(M):
    A = sorted(A, key= lambda x: (-x[0], x[2]))
    for i in range(N):
        f = A[2*i] 
        g = A[2*i+1]
        if (g[1][k] == 'G') and (f[1][k] == 'C'):
            g[0] += 1
        elif (g[1][k] == 'G') and (f[1][k] == 'P'):
            f[0] += 1
        elif (g[1][k] == 'C') and (f[1][k] == 'G'):
            f[0] += 1
        elif (g[1][k] == 'C') and (f[1][k] == 'P'):
            g[0] += 1
        elif (g[1][k] == 'P') and (f[1][k] == 'G'):
            g[0] += 1
        elif (g[1][k] == 'P') and (f[1][k] == 'C'):
            f[0] += 1
        else:
            continue

A = sorted(A, key= lambda x: (-x[0], x[2]))
for a in A:
    print(a[2]+1)



