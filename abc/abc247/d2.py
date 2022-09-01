q = int(input())

ire = list() # [naniwo, nanko]
dasu = list() # nanko
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
        elif ire[k][1] == 0:
            continue
        elif ire[k][1] > nokori:
            ans += ire[k][0]*nokori
            ire[k][1] = ire[k][1] - nokori
            nokori = 0
            break
        else:
            ans += ire[k][0] * ire[k][1]
            nokori = nokori - ire[k][1]
            ire[k][1] = 0
    print(ans)
    
