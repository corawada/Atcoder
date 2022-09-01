from itertools import combinations
n, m = map(int, input().split())


ans_list = list()
for i in combinations(list(range(1, m+1)), n):
    ans_list.append(i)

ans_list = sorted(ans_list)

for ans in ans_list:
    print(' '.join([str(k) for k in ans]))


