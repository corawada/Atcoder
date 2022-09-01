import math

n = int(input())

pre_prime_nums = [i for i in range(2, math.ceil(n**(1/3)))]
prime_nums = list()
prime_nums_dic = dict()

def uekara_search(x, jogen):
    while True:
        # print(x, prime_nums[jogen])
        if x >= prime_nums[jogen]:
            # print(p, x, jogen)
            return jogen
        jogen -= 1

numbers = 0
for k in pre_prime_nums:
    for pn in prime_nums:
        if k % pn == 0:
            break
    else:
        prime_nums.append(k)
        prime_nums_dic[k] = numbers
        numbers += 1

ans = 0

# print(prime_nums)
print(len(prime_nums))
"""
jogen = numbers - 1
# print(jogen)
for p in prime_nums:
    Q = math.floor((n/p)**(1/3) + 10**(-8))
    # print("p:{:3d} , Q:{:3d} -----".format(p, Q))
    if p >= Q:
        continue
    else:
        jogen = uekara_search(Q, jogen)
        # print("jogen : {}".format(jogen))
        ans += max(0, jogen - prime_nums_dic[p])
        # print(max(0, jogen - prime_nums_dic[p]))

print(ans)
"""
