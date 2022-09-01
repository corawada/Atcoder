from collections import defaultdict
from itertools import combinations

n, m = map(int, input().split())

hen = defaultdict(set)

for _ in range(m):
    a, b = map(int, input().split())
    hen[a].add(b)
    hen[b].add(a)

count = 0
for h in hen.values():
    if len(h) < 2:
        continue
    else:
        for a, b in combinations(h, 2):
            if b in hen[a]:
                count += 1

print(count//3)

