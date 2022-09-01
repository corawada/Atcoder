from math import sqrt

n = int(input())

nn = set()

for i in range(2, int(sqrt(n)) + 1):
    k = 2
    while True:
        if i ** k <= n:
            nn.add(i**k)
            k += 1
        else:
            break

print(n-len(nn))



