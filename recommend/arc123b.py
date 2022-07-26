from collections import deque
n = int(input())

A = sorted(list(map(int, input().split())))
B = deque(sorted(list(map(int, input().split()))))
C = deque(sorted(list(map(int, input().split()))))

ans = 0
for a in A:
    while B:
        b = B.popleft()
        if a < b:
            while C:
                c = C.popleft()
                if b < c:
                    ans += 1
                    break
            break
        else:
            continue

print(ans)
