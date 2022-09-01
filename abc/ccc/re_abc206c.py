from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

all_num = defaultdict(int)
ans = 0
for idx, a in enumerate(reversed(A)):
    all_num[a] += 1
    ans += idx - all_num[a] + 1

print(ans)

