n = int(input())
A = list(map(int, input().split()))
last = 0
rui = list()

max_foot = -10**10
for a in A:
    last += a
    max_foot = max(max_foot, last)
    rui.append([last, max_foot])

now = 0
now_max = 0
for r, m in rui:
    now += r
    now_max = max(now_max, now, now+m-r)

print(now_max)


