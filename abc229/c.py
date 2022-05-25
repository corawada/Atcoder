N, W = map(int, input().split())

cheese = []

for _ in range(N):
    a, b = map(int, input().split())
    cheese.append([a, b])

cheese = sorted(cheese, key=lambda x : x[0])

ans = 0
while cheese:
    ch = cheese.pop()
    ans += min(W, ch[1]) * ch[0]
    W -= min(W, ch[1])
    if W == 0:
        break
    
print(ans)

