S = input()

str_dic = {'a':0, 'b':0, 'c':0}

for s in S:
    str_dic[s] += 1

S_chr = list()
for key, value in str_dic.items():
    S_chr.append(value)


if S_chr[0] - S_chr[1] == 0:
    if S_chr[0] - S_chr[2] == 0:
        print('YES')
    elif S_chr[0] - S_chr[2] == 1:
        print('YES')
    elif S_chr[0] - S_chr[2] == -1:
        print('YES')
    else:
        print('NO')
elif S_chr[0] - S_chr[1] == 1:
    if S_chr[0] - S_chr[2] == 0:
        print('YES')
    elif S_chr[0] - S_chr[2] == 1:
        print('YES')
    else:
        print('NO')
elif S_chr[0] - S_chr[1] == -1:
    if S_chr[0] - S_chr[2] == 0:
        print('YES')
    elif S_chr[0] - S_chr[2] == -1:
        print('YES')
    else:
        print('NO')
else:
    print('NO')



# timestamp
# Data     Time     Diff     msg
# 22/07/11 20:45:44 00:00:00 start
# 22/07/11 21:57:47 01:12:03 submit
