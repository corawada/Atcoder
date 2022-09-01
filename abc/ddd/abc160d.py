from collections import defaultdict
n, x, y = map(int, input().split())

for k in range(1, n):
    count = 0 
    for i in range(1, n+1):
        set_pre_j = set()
        set_pre_j.add(k + i)
        set_pre_j.add(k - abs(i-x) - 1 + y)
        set_pre_j.add(-k + abs(i-x) + 1 + y)
        for j in set_pre_j:
            if i < j <= n:
                choku = j - i 
                xy_kei = abs(i-x) + abs(j-y) + 1
                if k == min(choku, xy_kei):
                    count += 1

    print(count)
