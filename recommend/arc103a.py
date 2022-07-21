from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

kind_a = defaultdict(int)
kind_b = defaultdict(int)

for idx, a in enumerate(A):
    if idx%2 == 0:
        kind_a[a] += 1
    else:
        kind_b[a] += 1

list_a = list()
list_b = list()
for key, value in kind_a.items():
    list_a.append([value, key])

for key, value in kind_b.items():
    list_b.append([value, key])

list_a = sorted(list_a)
list_b = sorted(list_b)

if list_a[-1][1] != list_b[-1][1]:
    ans = n - list_a[-1][0] - list_b[-1][0]
elif (len(list_a) == 1) and (len(list_b) == 1):
    ans = n//2
elif len(list_a) == 1:
    ans = n//2 - list_b[-2][0]
elif len(list_b) == 1:
    ans = n//2 - list_a[-2][0]
else:
    ans_a = n - list_a[-1][0] - list_b[-2][0]
    ans_b = n - list_a[-2][0] - list_b[-1][0]
    ans = min(ans_a, ans_b)

print(ans)

