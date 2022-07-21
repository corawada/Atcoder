n = int(input())

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
    arr = 1
    temp = n
    for i in prime_nums:
        if temp%i == 0:
            cnt = 0
            while temp%i == 0:
                cnt += 1
                temp //= i
            arr+=cnt
        if temp==1:
            break
    if temp!=1:
        arr += 1
    return arr

ans = list()
for i in range(1, n+1):
    ans.append(up_factorizaiton(i))

print(' '.join([str(k) for k in ans]))



    
