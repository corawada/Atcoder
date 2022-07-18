n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

diff = 0
for a, b in zip(A, B):
    diff += abs(a-b)

if k >= diff:
    if (k-diff)%2 == 0:
        print('Yes')
    else:
        print('No')
else:
    print('No')

# timestamp
# Data     Time     Diff     msg
# 22/07/14 17:24:15 00:00:00 start
# 22/07/14 17:27:37 00:03:22 submit
