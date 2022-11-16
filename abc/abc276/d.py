n = int(input())
A = list(map(int, input().split()))

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)


gcd_a = A[-1]
for a in A:
    gcd_a = gcd(gcd_a, a)

counter = 0
flag = True
for a in A:
    a //= gcd_a

    while flag:
        if a % 2 == 0:
            counter += 1
            a //= 2
        elif a % 3 == 0:
            counter += 1
            a //= 3
        else:
            flag = False

    if (flag == False) and (a != 1):
        print(-1)
        break
    
    flag = True
else:
    print(counter)

