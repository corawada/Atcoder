# 素数判定
# 使いまわさない用
import math
def jadge_prime_num(x):
    if x == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(x))+1):
        if x % i == 0:
            return False
    else:
        return True

# 使い回す用
# 2の倍数を非処理にする
import math
def jadge_prime_num2(x):
    if x % 2 == 0:
        if x == 2:
            return True
        else:
            return False
    elif x == 3:
        return True
    # for i in range(1, math.ceil(math.sqrt(x))//2+1):
    for i in range(3, math.ceil(math.sqrt(x))+1, 2):
        # if x %(2*i+1) == 0:
        if x % i == 0:
            return False
    else:
        return True

# 素数生成
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

print(len(prime_nums))


