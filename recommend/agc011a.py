from collections import deque
n, c, k = map(int, input().split())

A = list()
for _ in range(n):
    A.append(int(input()))
    
A = sorted(A)
que = deque()
que_len = 0

ans = 0

for a in A:

    if que:
        if a - first_n > k:
            ans += 1
            que = deque()
            que_len = 1
            que.append(a)
            first_n = a
        else:
            que.append(a)
            que_len += 1
        
    else:
        que_len = 1
        que.append(a)
        first_n = a

    if que_len == c:
        ans += 1
        que = deque()
        que_len = 0
else:
    if que:
        ans += 1


print(ans)

