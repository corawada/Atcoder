import itertools
N, M = map(int, input().split())

taka = list()
aoki = list()

for _ in range(M):
    taka.append(list(map(int, input().split())))

for _ in range(M):
    aoki.append(list(map(int, input().split())))

aoki = sorted(aoki)

for i in itertools.permutations(range(1, N+1)):
    cp_taka = list()
    for a, b in taka:
        cp_taka.append(sorted([i[a-1], i[b-1]]))
    cp_taka = sorted(cp_taka)
    if cp_taka == aoki:
        print('Yes')
        break
else:
    print('No')

