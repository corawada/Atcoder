import math

n = int(input())

prime_=[True]*(10**6+1)
prime_[0]=False
prime_[1]=False
for i in range(2,10**3+1):
  if prime_[i]:
    for j in range(2*i,10**6+1,i):
      prime_[j]=False
prime_nums=[]
prime_nums_dic = dict()
numbers = 0
for i in range(10**6+1):
  if prime_[i]:
    prime_nums.append(i)
    prime_nums_dic[i] = numbers
    numbers += 1

def uekara_search(x, jogen):
    while True:
        # print(x, prime_nums[jogen])
        if x >= prime_nums[jogen]:
            # print(p, x, jogen)
            return jogen
        jogen -= 1


ans = 0

# print(prime_nums)
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
