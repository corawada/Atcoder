n = int(input())

xandy = list()

for _ in range(n):
    x, y = map(int, input().split())
    xandy.append([x, y])

# print(xandy)

direc = str(input())

hito = dict()
for i, v in enumerate(direc):
    list_xy = xandy[i]
    list_xy.append(v)

    if list_xy[1] in hito:
        tmp = hito[list_xy[1]]
        tmp.update({list_xy[0]:v})
    else:
        hito[list_xy[1]] = {list_xy[0]:v}

# print(hito)

ans = "No"
for v in hito.values():
    v = sorted(v.items())
 #    print(v)

    flag = False
    for val in v:
        if val[-1] == 'L':
            if flag == True:
                ans = "Yes"
            else:
                pass
        else:
            flag = True

print(ans)











