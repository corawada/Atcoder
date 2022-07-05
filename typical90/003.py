# おまじない
import sys
sys.setrecursionlimit(10**6)


from collections import defaultdict
import time

n = int(input())
Tree = defaultdict(list)

for _ in range(n-1):
    a, b = map(int, input().split())
    Tree[a].append(b)
    Tree[b].append(a)

# print(Tree)

def dfs(node_num, depth) -> (int, int):
    global u, max_depth
    # print('call node: {}  depth: {}'.format(node_num, depth))
    # time.sleep(1)
    if stack[node_num] == 1:
        # print('this node was already searched')
        return depth - 1

    else:
        # 条件分岐でuの更新
        if depth - 1 > max_depth:
            max_depth = depth - 1
            u = node_num


        stack[node_num] = 1
        pre_ans = 0
        for k in Tree[node_num]:
            
             pre_ans = max(pre_ans, dfs(k, depth+1))
        return pre_ans

    

# node 1 から最も遠い頂点uを探索する
stack = [0]*(n+1)
u = 0
max_depth = 0
dfs(2, 1)

# print(u)

# node u から最も遠い頂点vを探索する

stack = [0]*(n+1)
print(dfs(u, 1))




