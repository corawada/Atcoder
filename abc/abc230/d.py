n, d = map(int, input().split())

sec = list()
for _ in range(n):
    l, r = map(int, input().split())
    sec.append([l, r])

sec = sorted(sec, key=lambda x: x[1])

last_punch = -10**10
count = 0

for se in sec:
    if last_punch + d <= se[0]:
        last_punch = se[1]
        count += 1
    else:
        continue

print(count)
