k = int(input())

kai = {0:1}

for i in range(1, 11):
    kai[i] = kai[i-1] * i

ans = 0

for j in range(10, 0, -1):
    tmp = k//kai[j]
    ans += tmp
    k = k%kai[j]

print(ans)
