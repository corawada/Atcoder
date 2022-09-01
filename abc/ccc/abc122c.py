from bisect import bisect_right, bisect_left
n, q = map(int, input().split())
A = input()

ac_list = list()
flag = False
for idx, a in enumerate(A):
    if a == 'A':
        flag = True
    elif flag and (a=='C'):
        ac_list.append(idx)
        flag = False
    else:
        flag = False

for _ in range(q):
    l, r = map(int, input().split())
    l_c = bisect_left(ac_list, l)
    r_c = bisect_right(ac_list, r-1)
    print(r_c-l_c)
