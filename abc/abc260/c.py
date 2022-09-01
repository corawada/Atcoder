N, X, Y = map(int, input().split())

# Rn => R(n-1) & X * Bn
# Bn =+ R(

R = [0] * 10
R[N-1] = 1
B = [0] * 10

for i in range(9, 0, -1):
    R[i-1] += R[i]
    B[i] += R[i] * X
    R[i-1] += B[i]
    B[i-1] += B[i] * Y


print(B[0])
