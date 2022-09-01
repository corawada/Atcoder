from collections import deque

q = int(input())

ire = deque() # [naniwo, nanko]
dasu = deque() # nanko

for i in range(q):
    query = input().split()
    if query[0] == "1":
        ire.append([int(query[1]), int(query[2])])
    else:
        dasu.append(int(query[1]))

for j in range(len(dasu)):
    nokori = dasu[j]
    ans = 0
    for k in range(len(ire)):
        if nokori == 0:
            break
        elif ire[0][1] == 0:
            continue
        elif ire[0][1] > nokori:
            ans += ire[0][0]*nokori
            ire[0][1] = ire[0][1] - nokori
            nokori = 0
            break
        else:
            ans += ire[0][0] * ire[0][1]
            nokori = nokori - ire[0][1]
            ire.popleft()
    print(ans)
    
