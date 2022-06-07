def prime_f_dict(num):
    divisors={}
    prime=2
    while(prime <= num):
        expon=0
        while(num % prime == 0):
            expon+=1
            num //= prime
        if expon != 0:
            divisors[prime]=expon
        prime += 1
    print(divisors)
    return divisors

def multi_num(num):
    nu_dic = prime_f_dict(num)
    ans = 1
    for v in nu_dic.values():
        ans = ans*(v+1)
    print(ans)
    return ans

n = int(input())

ans = 0
for i in range(2,n+1):
    print('-'*10 + ' {} '.format(i))
    for m in ramge(multi_num(i*i)):

print(ans)
