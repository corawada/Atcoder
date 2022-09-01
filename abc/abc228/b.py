n, x = map(int, input().split())
A = list(map(int, input().split()))
Aknow = [0] * (n+1)

num = 0
while True:
    if Aknow[x] == 0:
        Aknow[x] = 1
        x = A[x-1]
        num += 1
    else:
        break

print(num)

