N, P = map(int, input().split())

A = list(map(int, input().split()))

ans = 0
for _ in range(N):
    if A.pop() < P:
        ans += 1

print(ans)
