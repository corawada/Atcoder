# おまじない
import sys
sys.setrecursionlimit(100000)

from collections import defaultdict
n = int(input())

tree = defaultdict(set)

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].add(b)
    tree[b].add(a)

node_col = [None]*(n+1)

col_num = {0:list(), 1:list()}
def bfs(node, col):
    node_col[node] = col
    col_num[col].append(node)
    for i in tree[node]:
        if node_col[i] is not None:
            continue
        bfs(i, 1 - col)

bfs(1, 0)

if len(col_num[0]) > len(col_num[1]):
    print(' '.join([str(i) for i in col_num[0][:n//2]]))
else:
    print(' '.join([str(i) for i in col_num[1][:n//2]]))


