from collections import deque

n = int(input())
H = deque(map(int, input().split()))

a = H.popleft()
for _ in range(n-1):
    b = H.popleft()
    if a < b:
        a = b
    else:
        break

print(a)
