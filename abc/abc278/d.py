n = int(input())

A = list(map(int, input().split()))
a_dic = dict()
flag_dic = dict()

i = 1
for a in A:
    a_dic[i] = a
    flag_dic[i] = -1
    i += 1

q = int(input())

init_num = -1
init = 0
for i in range(q):
    query = list(map(int, input().split()))
    # print(query)

    if query[0] == 1:
        init = query[1]
        init_num = i

    elif query[0] == 2:
        if flag_dic[query[1]] == init_num:
            a_dic[query[1]] += query[2]
        else:
            flag_dic[query[1]] = init_num
            a_dic[query[1]] = init + query[2]

    else:
        if flag_dic[query[1]] == init_num:
            print(a_dic[query[1]])
        else:
            print(init)

