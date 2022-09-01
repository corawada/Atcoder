n, k = map(int, input().split())

A = set()
a_dic = dict()

for _ in range(n):
    a, b = map(int, input().split())
    if a in a_dic:
        a_dic[a] += b
    else:
        a_dic[a] = b
    A.add(a)

sort_A = sorted(list(A))

for a in sort_A:
    k -= a_dic[a]
    if k <= 0:
        print(a)
        break
