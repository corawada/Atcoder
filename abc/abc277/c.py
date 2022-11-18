from collections import defaultdict
n = int(input())

ladders = defaultdict(set)

for _ in range(n):
    a, b = map(int, input().split())
    ladders[a].add(b)
    ladders[b].add(a)

stack = {1, }
already = {1, }

while stack:
    s = stack.pop()
    for lad in ladders[s]:
        if lad not in already:
            stack.add(lad)
            already.add(lad)

print(max(already))




