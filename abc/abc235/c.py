N, Q = map(int, input().split())
a = list(map(int, input().split()))

dic = {}
for i, j in zip(a, range(N)):
    if i in dic:
        dic[i].append(j)
    else:
        dic[i] = [j]

for _ in range(Q):
    X, K = map(int, input().split())
    if X in dic:
        if len(dic[X]) < K:
            print(-1)
        else:
            print(dic[X][K-1] + 1)
    else:
        print(-1)

