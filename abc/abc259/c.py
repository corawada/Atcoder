from collections import deque
S = deque(input())
T = deque(input())

list_t = deque()
from_t = T.popleft()
count = 1
for _ in range(len(T)):
    t = T.popleft()
    if t == from_t:
        count += 1
    else:
        list_t.append([from_t, count])
        from_t = t
        count = 1
else:
    list_t.append([t, count])

list_s = deque()
from_s = S.popleft()
count = 1
#for s in S:
for _ in range(len(S)):
    s = S.popleft()
    if s == from_s:
        count += 1
    else:
        list_s.append([from_s, count])
        from_s = s
        count = 1
else:
    list_s.append([s, count])

if len(list_t) == len(list_s):
    while list_t and list_s:
        ss = list_s.popleft()
        tt = list_t.popleft()
        if ss[0] != tt[0]:
            print('No')
            break
        elif ss[1] == tt[1]:
            continue
        elif (ss[1] > 1) and (tt[1] > 2) and (ss[1] < tt[1]):
            continue
        else:
            print('No')
            break
    else:
        print('Yes')
else:
    print('No')
