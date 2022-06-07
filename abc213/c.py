H, W, N = map(int, input().split())

A = list()
B = list()

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

sort_A = sorted(set(A))[::-1]

sort_dic_A = dict()
idx = 1
for _ in range(len(sort_A)):
    sort_dic_A[sort_A.pop()] = idx
    idx += 1

sort_B = sorted(set(B))[::-1]
sort_dic_B = dict()
idx = 1
for _ in range(len(sort_B)):
    sort_dic_B[sort_B.pop()] = idx
    idx += 1

re_A = list()
re_B = list()
for _ in range(N):
    a = A.pop()
    re_A.append(sort_dic_A[a])

    b = B.pop()
    re_B.append(sort_dic_B[b])


for _ in range(N):
    print("{} {}".format(re_A.pop(), re_B.pop()))




