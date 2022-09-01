from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))
mod = 998244353

ans_multi = list()
a_dic = defaultdict(int)


if A[0] != 0:
    print(0)
else:
    for a in A:
        a_dic[a] += 1

    flag = False
    for i in range(n):
        if i in a_dic:
            if flag:
                print(0)
                break
            else:
                continue
        else:
            flag = True
    else:
        if a_dic[0] == 1:
            ans = 1
            for i in range(2, max(A)+1):
                ans *= a_dic[i-1]**a_dic[i]
                ans %= mod

            print(ans)
        else:
            print(0)




