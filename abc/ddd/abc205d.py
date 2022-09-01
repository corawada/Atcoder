from bisect import bisect_right
n, q = map(int, input().split())
A = list(map(int, input().split()))

rank_dic = {1:1}
max_key = 1
max_value = 1

rank_list = [1,]
for idx, a in enumerate(A):
    if a == max_value:
        rank_dic[max_key] = a+1
        max_value = a+1

    else:
        rank_dic[a-idx] = a+1
        max_key = a-idx
        max_value = a+1
        rank_list.append(max_key)

for _ in range(q):
    inp = int(input())
    k = rank_list[bisect_right(rank_list, inp)-1]
    print(rank_dic[k] + inp - k)

# timestamp
# Data     Time     Diff     msg
# 22/07/12 21:17:45 00:00:00 start
# 22/07/12 21:21:40 00:03:55 submit re
