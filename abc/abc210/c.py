from collections import deque
n, k = map(int, input().split())
nn = deque(map(int, input().split()))

cdeque = deque([nn.popleft() for _ in range(k)])
ans = [len(set(cdeque))]
for i in range(n-k):
    cdeque.popleft()
    cdeque.append(nn.popleft())
    ans.append(len(set(cdeque)))

print(max(ans))


