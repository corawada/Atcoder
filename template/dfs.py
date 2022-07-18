# おまじない 
import sys
sys.setrecursionlimit(10000)
# sys.setrecursionlimit(1000000)

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

