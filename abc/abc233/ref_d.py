# 32705867
# D - Count Interval
# https://atcoder.jp/contests/abc233/tasks/abc233_d

# from collections import Counter


from collections import defaultdict


n, k = map(int, input().split())
A = list(map(int, input().split()))
# print(A)

rui = [0] * (n + 1)
# print(rui)

for i in range(n):
    rui[i + 1] = rui[i] + A[i]
# print(rui)

C = defaultdict(int)

for r in rui:
    C[r] += 1

# print(C)

# C = Counter(rui)

ans = 0
for r in rui:
    # print(r)
    C[r] -= 1
    ans += C[r + k]

print(ans)

