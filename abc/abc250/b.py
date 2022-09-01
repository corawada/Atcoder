N, A, B = map(int, input().split())

ans = ""

shiro = ""
kuro = ""
flag = 0
for _ in range(N):
    if flag%2==0:
        shiro += "." * B
        kuro += "#" * B
    else:
        shiro += "#" * B
        kuro += "." * B
    flag += 1


flag = 0
for _ in range(N):
    if flag % 2 == 0:
        for i in range(A):
            print(shiro)
    else:
        for i in range(A):
            print(kuro)
    flag += 1
        

