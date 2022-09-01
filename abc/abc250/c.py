N, Q = map(int, input().split())
fi = [i for i in range(0, N+1)]
fn = [i for i in range(0, N+1)]

for _ in range(Q):
    x = int(input())
    adress = fi[x]
    if adress != N:
        nb = fn[adress+1]
        fi[x] = adress + 1
        fi[nb] = adress
        fn[adress] = nb
        fn[adress+1] = x
    else:
        fb = fn[adress-1]
        fi[x] = adress-1
        fi[fb] = adress
        fn[adress] = fb
        fn[adress-1] = x

for i in fn:
    if i == 0:
        continue
    else:
        print(i, end=" ")



