n = int(input())
A = list(map(int, input().split()))
Q = int(input())

A_dic = dict()
for idx, a in enumerate(A):
    if a not in A_dic:
        A_dic[a] = [0, idx]
    else:
        A_dic[a].append(idx)

# print(A_dic)


def binary_search(tar_l, tar_r, tar_lis):
    bs = tar_lis.copy()
    bs.append(2 * (10**5) + 1)
    bs.append(2 * (10**5) + 2)

    # print('from {} to {} ----- search : {}'.format(tar_l, tar_r, bs))
    # l 側を決める
    l = 0
    r = len(bs) - 1
    while (r -l) > 1:
        i = (l + r) // 2
        if bs[i] < tar_l:
            l = i 
        elif bs[i] > tar_l:
            r = i 
        else:
            l = i - 1
            break
    ll = l

    # r 側を決める
    # l = ll
    r = len(bs) - 1
    while (r -l) > 1:
        i = (l + r) // 2
        if bs[i] < tar_r:
            l = i 
        elif bs[i] > tar_r:
            r = i 
        else:
            # l = i - 1
            l = i 
            break
    rr = l

    # print(ll, rr)

    return rr - ll



for _ in range(Q):
    L, R, X = map(int, input().split())
    # print('query -- from {} to {} -- search {}'.format(L, R, X))
    if X in A_dic:
        # print('atta')

        print(binary_search(L-1, R-1, A_dic[X]))


    else:
        print(0)

