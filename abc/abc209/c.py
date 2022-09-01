n = int(input())
C = sorted(list(map(int, input().split())))

ans = 1
for idx, val in enumerate(C):
    ans = (ans*(val-idx))%(10**9+7)

print(ans%(10**9+7))

