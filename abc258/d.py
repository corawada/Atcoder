from collections import deque
n, x = map(int, input().split())

task = deque()
rui = deque([0,])
for _ in range(n):
    a, b = map(int, input().split())
    task.append([a, b])
    rui.append(rui[-1] + a + b)

rui.popleft()

ans = 10 ** 30
for i in range(n):
    if i == x - 1:
        break
    a, b = task.popleft()
    c = rui.popleft()
    ans = min(ans, c + b*(x-i-1))

print(ans)


    


