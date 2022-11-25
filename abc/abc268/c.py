from collections import defaultdict
n = int(input())

P = list(map(int, input().split()))

ans = defaultdict(int)

for i, p in enumerate(P):
    ans[(i-1-p)%n] += 1
    ans[(i-p)%n] += 1
    ans[(i+1-p)%n] += 1

print(max(ans.values()))

