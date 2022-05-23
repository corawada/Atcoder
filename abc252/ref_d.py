#31635907
from collections import deque

N = int(input())
A = list(map(int, input().split()))

A_mm = deque()
for a in A:
    big_a = 0
    small_a = 0
    A_d = deque(A)
    for _ in range(N):
        b = A_d.pop()
        if a < b:
            big_a+=1
        elif a > b:
            small_a += 1
        else:
            pass
    A_mm.append([big_a, small_a])

ans = 0

for _ in range(len(A)):
    pacho = A_mm.pop()
    ans += pacho[0] * pacho[1]

print(ans)
