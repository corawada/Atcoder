import random
n = int(input())

def func(n):
    ans = 0
    for i in range(len(str(n))):
        if i == len(str(n)) - 1:
            end = n - 10**(i) + 1
        else:
            end = 10 ** (i+1) - 10**(i) 
        ans += (((1 + end)*end)//2) % 998244353
    return ans%998244353

print(func(n))

