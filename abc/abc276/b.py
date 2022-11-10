from collections import defaultdict

n, m = map(int, input().split())

city = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    city[a].append(b)
    city[b].append(a)

for i in range(1, n+1):
    if i in city:
        ans_list = sorted(city[i])
        print(len(ans_list), " ".join([str(k) for k in ans_list]) )

    else:
        print(0)

