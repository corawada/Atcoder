h, w = map(int, input().split())
n = int(input())
A = list(map(int, input().split()))

a_lis = []

for idx, a in enumerate(A):
    for _ in range(a):
        a_lis.append(idx+1)

a_lis = a_lis[::-1]

ans = list()
for i in range(h):
    pre_ans = list()
    for _ in range(w):
        pre_ans.append(str(a_lis.pop()))
    if i % 2 == 0:
        ans.append(pre_ans)
    else:
        ans.append(pre_ans[::-1])

for an in ans:
    print(' '.join(an))

