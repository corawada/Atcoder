from collections import defaultdict
n, m = map(int, input().split())
mod = 10**9 + 7

graph = defaultdict(set)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

print(graph)

#bfs
already = {1, }
stack = {1, }
while stack and (n not in already):
    next_stack = {}
    for tar in stack:
        for 
        

