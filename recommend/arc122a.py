n = int(input())
A = list(map(int, input().split()))

mod = (10**9) + 7

ans = 0
for bit in range(2**(n-1)):
    bitstr = "{bit:0{numlen}b}".format(bit=bit, numlen=n-1)
    tmp_ans = A[0]
    pre_s = '0'
    for s, num in zip(bitstr, A[1:]):
        if s == '0':
            tmp_ans += num
        else:
            if pre_s == '1':
                break
            tmp_ans -= num

        pre_s = s
    else:
        print(bitstr)
        # print(tmp_ans)
        ans += tmp_ans % mod

print(ans % mod)



    
