N = int(input())

T = [list(map(int, input().split())) for _ in range(N-1)]


p = T.pop()
a , b = p[0] , p[1]

p2 = T.pop()
a2, b2 = p2[0], p2[1]

flag = False
if a in p2:
    g = a
    while T:
        if g not in T.pop():
            break
    else:
        flag = True
if b in p2:
    g = b
    while T:
        if g not in T.pop():
            break
    else:
        flag = True
else:
    pass

if flag:
    print("Yes")
else:
    print("No")
