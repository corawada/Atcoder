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
            arr.append(i)

        if temp==1:
            break

    if temp!=1:
        arr.append(temp)

    if arr==[]:
        arr.append(n)

    return arr

a, b = map(int, input().split())

a_div = up_factorizaiton(a)
b_div = set(up_factorizaiton(b))

ans = 1
for ad in a_div:
    if ad in b_div:
        ans += 1

if (a==1) and (b==1):
    ans = 1
print(ans)
