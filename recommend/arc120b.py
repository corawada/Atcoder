from pprint import pprint
from collections import defaultdict
h, w = map(int, input().split())
mod = 998244353

nn = defaultdict(set)
for i in range(h):
    S = input()
    for j, s in enumerate(S):
        nn[i+j].add(s)

ans = 1
for set_n in nn.values():
    if ('B' in set_n) and ('R' in set_n):
        ans = 0
    elif {'.'} == set_n:
        ans *= 2
        ans %= mod


print(ans)

