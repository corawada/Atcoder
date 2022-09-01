a, b, c, d = map(int, input().split())

import math
def jadge_prime_num(x):
    if x == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(x))+1):
        if x % i == 0:
            return False
    else:
        return True

for i in range(a, b+1):
    for j in range(c, d+1):
        if jadge_prime_num(i+j):
            break
    else:
        print('Takahashi')
        break
else:
    print('Aoki')


