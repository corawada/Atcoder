from bisect import bisect_left
n, p, q, r = map(int, input().split())
A = list(map(int, input().split()))
rui = [0, ]
rui_set = set()

for a in A:
    tmp = rui[-1] + a
    rui.append(tmp)
    rui_set.add(tmp)

flag = False
for xr in rui:
    if xr+p in rui_set:
    # if p-xr in rui_set:
        # y の判定
        tar_y = bisect_left(rui, xr+p)
        for yr in rui[tar_y:]:
            if yr+q in rui_set:
            # if yr-q in rui_set:
                # z の判定
                tar_z = bisect_left(rui, yr+q)
                for zr in rui[tar_z:]:
                    # if zr-r in rui_set:
                    if zr+r in rui_set:
                        flag = True
                        print('Yes')
                        break
                if flag:
                    break

        if flag:
            break
else:
    print('No')




    


