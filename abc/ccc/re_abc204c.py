from collections import defaultdict
n, m = map(int, input().split())

graph = defaultdict(set)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)

ans = 0

for i in range(1, n+1):
    already = {i, }
    stack = {i, }
    while stack:
        j = stack.pop()
        for k in graph[j]:
            if k in already:
                continue
            else:
                already.add(k)
                stack.add(k)
    ans += len(already)

print(ans)




