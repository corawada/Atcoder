import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())

load_l = [[] for _ in range(n)]


for _ in range(m):
    a, b = map(int, input().split())
    load_l[a-1].append(b-1)

ans = 0

def dfs(city_n):
    global ans 
    if city_n in visit_set:
        return

    visit_set.add(city_n)
    ans += 1

    visit_cue = set(load_l[city_n])

    for c in visit_cue:
        dfs(c)
    return

for i in range(n):
    visit_set = set()
    dfs(i)

print(ans)

