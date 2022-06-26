import math
import itertools

n = int(input())

pre_prime_nums = [i for i in range(2, math.ceil(n**(1/3)) + 1)]
prime_nums = list()

for k in pre_prime_nums:
    for pn in prime_nums:
        if k % pn == 0:
            break
    else:
        prime_nums.append(k)

ans = 0

def binary_search(x):
    l = 0
    r = len(prime_nums) - 1
    while (r-l) > 1:
        i = (r + l )//2
        if x < prime_nums[i]:
            r = i
        elif x > prime_nums[i]:
            l = i
        else:
            l = i
            break
    return l

for idx, p in enumerate(prime_nums):
    ans += max(0, binary_search((n/p) ** (1/3)) - idx)

print(ans)


        




