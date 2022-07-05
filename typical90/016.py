import math
n = int(input())
a, b, c = sorted(list(map(int, input().split())))

ans = 10000
for i in range(math.ceil(n//a)+2):
    for j in range(10000-i):
        if a*i + b*j > n: 
            break
        if (n-a*i-b*j)%c == 0:
            ans = min(ans, i+j+(n-a*i-b*j)//c)

print(ans)




