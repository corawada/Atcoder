import heapq
from collections import defaultdict
n, m, t = map(int, input().split())

A = list(map(int, input().split()))

loads = defaultdict(dict)
re_loads = defaultdict(dict)
for _ in range(m):
    a, b, c = map(int, input().split())
    loads[a][b] = c
    re_loads[b][a] = c

INF = 10 ** 10
costs = []
heapq.heappush(costs, (1, 0))
dist = [INF] * (n+1)
re_dist = [INF] * (n+1)

while costs:
    tar_city, so_far_cost = heapq.heappop(costs)
    if dist[tar_city] < so_far_cost: continue

    dist[tar_city] = so_far_cost
    for city, tmp_cost in loads[tar_city].items():
        if dist[city] <= so_far_cost + tmp_cost: 
            continue
        dist[city] = so_far_cost + tmp_cost

        heapq.heappush(costs, (city, so_far_cost+tmp_cost))

heapq.heappush(costs, (1, 0))

while costs:
    tar_city, so_far_cost = heapq.heappop(costs)
    if re_dist[tar_city] < so_far_cost: continue
    re_dist[tar_city] = so_far_cost
    for city, tmp_cost in re_loads[tar_city].items():
        if re_dist[city] <= so_far_cost + tmp_cost: 
            continue
        re_dist[city] = so_far_cost + tmp_cost
        heapq.heappush(costs, (city, so_far_cost+tmp_cost))

ans = 0
for i, a in enumerate(A):
    ans = max(ans, (t-dist[i+1]-re_dist[i+1])*a)

print(ans)

