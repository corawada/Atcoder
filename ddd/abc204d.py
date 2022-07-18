n = int(input())
T = list(map(int, input().split()))

T = sorted(T)

print(T)
ans_1 = 0
ans_2 = 0
print(sum(T))
for _ in range(n):
    t = T.pop()
    if ans_1 > ans_2:
        ans_2 += t
    else:
        ans_1 += t



print(max(ans_1, ans_2))
print(sum(T))
