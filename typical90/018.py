from math import sin, cos, pi, sqrt, atan, degrees

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())

for _ in range(Q):
    sita = 2* pi * (int(input()) % T) / T
    dis = sqrt(X**2 + (Y+(L*sin(sita)/2))**2)
    takasa = L*(1-cos(sita))/2
    print(degrees(atan(takasa/dis)))
