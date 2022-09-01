n, m = map(int, input().split())
A = set(map(int, input().split()))

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
    arr = set(); temp = n
    for i in prime_nums:
        if temp%i == 0:
            while temp%i == 0: temp //= i
            arr.add(i)
        if temp==1: break
    if temp!=1: arr.add(temp)
    if arr==[]: arr.add(n)
    return arr


prime_=[True]*(10**6+1)
prime_[0]=False
prime_[1]=False
jogai_prime = set()
for i in range(2,10**3+1):
    if prime_[i]:
        for j in range(2*i,10**6+1,i):
            if j in A:
                jogai_prime |= up_factorizaiton(j)
        if i in A:
            jogai_prime.add(i)

prime_=[True]*(10**6+1)
prime_[0]=False
prime_[1]=False
for i in range(2,10**3+1):
    if i in jogai_prime:
        for j in range(i,10**6+1,i):
            prime_[j]=False

next_prime_nums=[]
count = 1
for i in range(m+1):
    if prime_[i]:
        if (i not in jogai_prime) and (i not in A):
            count += 1
            next_prime_nums.append(i)

print(count)
print(1)
for p in next_prime_nums:
    print(p)

    
