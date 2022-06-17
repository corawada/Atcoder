n = int(input())

A = list(map(int, input().split()))

A_dic = dict()
for idx, a in enumerate(A):
    A_dic[a] = idx + 1

A = A[::-1]


for i in range(n-1):
    pre_A = list()

    for j in range(len(A) // 2):
        p = A.pop()
        q = A.pop()

        if p > q:
            pre_A.append(p)
        else:
            pre_A.append(q)

    A = pre_A[::-1]


if A[0] > A[1]:
    print(A_dic[A[1]])
else:
    print(A_dic[A[0]])





