from collections import deque
n = int(input())

S = deque(input())

sr = ""
sl = ""

while S:
    r = S.pop()
    l = S.popleft()
    
    while S:
        if r < l:
            sl += r
            sr += l
            break
        else:
            sl += l
            l = S.popleft()


ans = sl + sr[::-1]

print(ans)







# timestamp
# Data     Time     Diff     msg
# 22/07/26 23:25:25 00:00:00 start
