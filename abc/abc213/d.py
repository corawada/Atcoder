from collections import defaultdict

# おまじない
import sys
sys.setrecursionlimit(10000)

n = int(input())

tree = defaultdict(list)
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

pre_ans = list()

visited = [0]*(n+1)
def dfs(city):
    visited[city] = 1
    stock = sorted(tree[city])
    pre_ans.append(city)

    for c in stock:
        if visited[c] == 1:
            pass
        else:
            dfs(c)
            pre_ans.append(city)

dfs(1)

print(' '.join([str(i) for i in pre_ans]))

