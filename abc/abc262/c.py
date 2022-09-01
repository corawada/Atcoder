import sys
sys.setrecursionlimit(10000)

from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))


true_num = 0
tereco = defaultdict(int)
ans = 0
for idx, a in enumerate(A):
    if idx+1 == a:
        true_num += 1
    else:
        if a in tereco:
            if tereco[a] == idx+1:
                ans += 1
        
        tereco[idx+1] = a

ans += true_num*(true_num-1) // 2

print(ans)



