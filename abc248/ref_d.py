import bisect

n = int(input())
A = list(map(int, input().split()))
Q = int(input())

A_dic = dict()
for idx, a in enumerate(A):
    if a not in A_dic:
        A_dic[a] = [-1, idx+1]
    else:
        A_dic[a].append(idx+1)

for _ in range(Q):
    L, R, X = map(int, input().split())
    if X in A_dic:

        print((bisect.bisect_right(A_dic[X], R))-(bisect.bisect_left(A_dic[X], L)))

    else:
        print(0)

