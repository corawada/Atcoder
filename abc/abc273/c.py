from bisect import bisect_right

n = int(input())

A = list(map(int, input().split()))
a_so = sorted(list(set(A)))
len_a = len(a_so)

ans_dic = dict()
for a in A:
    an = len_a - bisect_right(a_so, a)
    if an in ans_dic:
        ans_dic[an] += 1
    else:
        ans_dic[an] = 1

for i in range(n):
    if i in ans_dic:
        print(ans_dic[i])
    else:
        print(0)

