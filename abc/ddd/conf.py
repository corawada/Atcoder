import heapq

N, M, T = map(int, input().split())
A = list(map(int, input().split()))
INF = 10**10

# 往路
G = [[] for _ in range(N)]
# 復路は辺の向きを変える
GR = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append((b, c))
    GR[b].append((a, c))

# 往路
dist = [INF] * N
dist[0] = 0
Q = []
heapq.heappush(Q, (dist[0], 0))
while Q:
    d, x = heapq.heappop(Q)
    if dist[x] < d: continue
    for nx, nd in G[x]:
        if dist[x] + nd >= dist[nx]: continue
        dist[nx] = dist[x] + nd
        heapq.heappush(Q, (dist[nx], nx))

# 復路
distR = [INF] * N
distR[0] = 0
QR = []
heapq.heappush(QR, (distR[0], 0))
while QR:
    d, x = heapq.heappop(QR)
    if distR[x] < d: continue
    for nx, nd in GR[x]:
        if distR[x] + nd >= distR[nx]: continue
        distR[nx] = distR[x] + nd
        heapq.heappush(QR, (distR[nx], nx))
# print(dist, distR)

ans = 0
for i in range(N):
    time = dist[i] + distR[i]
    money = A[i] * (T - time)
    ans = max(money, ans)

print(dist)
print(distR)

print(ans)
