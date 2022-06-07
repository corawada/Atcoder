N = int(input())

S = list(map(int, input().split()))
T = list(map(int, input().split()))

flag = True

while flag:
    flag = False
    for i, v in enumerate(S):
        I = (i+1) % N 
        if T[I] > T[i] + v:
            T[I] = T[i] + v
            flag = True

[print(p) for p in T]

