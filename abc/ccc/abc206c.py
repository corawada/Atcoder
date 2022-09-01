n = int(input())

A = list(map(int, input().split()))[::-1]

a_dic = dict()

re_ans = list()
for idx, a in enumerate(A):
    if a in a_dic:
        re_ans.append(idx - a_dic[a])
        a_dic[a] += 1
    else:
        re_ans.append(idx)
        a_dic[a] = 1

print(sum(re_ans))
