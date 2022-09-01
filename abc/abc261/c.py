n = int(input())

str_num = dict()
for _ in range(n):
    s = input()
    if s in str_num:
        print('{}({})'.format(s, str_num[s]))
        str_num[s] += 1
    else:
        print(s)
        str_num[s] = 1

