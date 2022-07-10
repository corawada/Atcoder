n = int(input())
l = len(str(n))

# print('l :', l)
ans = 0
lay_ans = 0
for i in range(1, l):
    lay_ans += 10**(i-1)
    ans += lay_ans

# print('now : ', ans)

for j in range(1, l+1):
    target = int('1'*j + '0'*(l-j))
    # print('j=', j, target, '-----')
    if n >= target:
        if str(n)[j-1] == '0':
            # print('koko')
            ans += 10**(l-j) 
        else:
            ans += min(int(str(n)[j-1:])-10**(l-j)+1, max(1,10**(l-j)))
            # print(str(n)[j-1:], 10**(l-j), 10**(l-j))
    else:
        break


# print('n', n)
print(ans)
    

# timestamp
# Data     Time     Diff     msg
# 22/07/08 19:52:20 00:00:00 first
# 22/07/08 21:21:35 01:29:15 first_2
# 22/07/08 22:40:31 02:48:11 1-append
