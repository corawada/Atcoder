n, m, t = map(int, input().split())


batte = n
pre_e = 0

for _ in range(m):
    s, e = map(int, input().split())
    
    batte = min(batte-s+pre_e, n)
    if batte <= 0:
        print("No")
        break
    else:
        batte = min(batte+e-s, n)

    pre_e = e
else:
    batte -= t - pre_e
    if batte <= 0:
        print("No")
    else:
        print("Yes")
