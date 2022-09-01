from collections import deque
n, m = map(int, input().split())
A = sorted(list(map(int, input().split())))
A = deque(A)

query = list()
for _ in range(m):
    b, c = map(int, input().split())
    query.append([c, b])

query = sorted(query)

ans = 0
flag = False
for _ in range(m):
    c, b = query.pop()
    for _ in range(b):
        if A:
            a = A.popleft()
            if a < c:
                ans += c
            else:
                ans += a
                flag = True
                break
        else:
            flag = True
            break

    if flag:
        break

if A:
    ans += sum(A)
print(ans)


