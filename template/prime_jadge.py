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
    for i in range(3, math.ceil(math.sqrt(x))+1, 2):
        if x % i == 0:
            return False
    else:
        return True


