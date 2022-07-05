n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B)

ans = 0
for a, b in zip(A, B):
    ans += abs(a-b)

print(ans)
