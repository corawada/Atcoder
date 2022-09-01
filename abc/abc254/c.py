N, K = map(int, input().split())

A = list()
div_lis = [[] for _ in range(K)]
index = 0
for i in input().split():
    A.append(int(i))
    div_lis[index].append(int(i))
    index = (index+1)% K

re_div_lis = []

for d in div_lis:
    re_div_lis.append(sorted(d)[::-1])

so_A = []
for i in range(N):
    so_A.append(re_div_lis[i%K].pop())

if so_A == sorted(A):
    print('Yes')
else:
    print('No')


