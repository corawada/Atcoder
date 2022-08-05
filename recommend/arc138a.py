from collections import deque
n, k = map(int, input().split())
A = list(map(int, input().split()))


left = deque(A[:k])
right = deque(A[k:])

ll = left.pop()
left.append(ll)
rr = right.popleft()
right.appendleft(rr)

ans = 1
while left or right:
    if left:
        pl = left.pop()
        if ll > pl:
            ll = pl
    if right:
        pr = right.popleft()
        if rr < pr:
            rr = pr







    if right and (ll < right.popleft()):
        break
    if left and (rr > left.pop()):
        break

    else:
        ans += 1
else:
    ans = -1

print(ans)



