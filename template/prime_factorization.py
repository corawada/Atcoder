# 一回だけの素因数分解
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

print(factorization(24))
# ==> [[2, 3], [3, 1]]


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
    for i in prime_nums:
        if temp%i == 0:
            cnt = 0
            while temp%i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

        if temp==1:
            break

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr


print(up_factorizaiton(2004))
print(len(prime_nums))
