from math import log, ceil
n = int(input())

ans = 0
if n == 0:
    ans = 0
elif n%2 == 0:
    for i in range(ceil(log(n)/log(5))):
        ans += (n//2)//(5**(i+1))

print(ans)

# timestamp
# Data     Time     Diff     msg
# 22/07/16 09:06:39 00:00:00 start
# 22/07/16 09:15:12 00:08:33 submit
# 22/07/16 09:18:52 00:12:13 AC
