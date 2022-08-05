# 素数テーブルを用いた素因数分解
prime_=[True]*(10**6+1)
prime_[0]=False
prime_[1]=False
for i in range(2,10**3+1):
    if prime_[i]:
        for j in range(2*i,10**6+1,i):
            prime_[j]=False
prime_nums=[]
for i in range(10**6+1):
    if prime_[i]:
        prime_nums.append(i)

def up_factorizaiton(n):
    arr = []
    temp = n
    ret = 1
    for i in prime_nums:
        if temp%i == 0:
            cnt = 0
            while temp%i == 0:
                cnt += 1
                temp //= i

            arr.append([i, cnt])

            if cnt%1 == 1:
                ret *= i

        if temp==1:
            break

    if temp!=1:
        arr.append([temp, 1])


    return ret


print(up_factorizaiton(24))
print(up_factorizaiton(122))
print(up_factorizaiton(3))
print(up_factorizaiton(1))

n = int(input())

heiho = {k**2 for k in range(1, (n+1)**2)}


ans = 0
# for i in range(1, n+1):
#     fc = up_factorizaiton(i)
#     ans += 1
#
#     # for j in range(1, n//fc + 1):
#     #     if j in heiho:
#     #         ans += 1
#
# print(ans)
