from math import gcd
n = int(input())

point = list()

vec_d = dict()
for _ in range(n):
    x, y = map(int, input().split())
    for p in point:
        a, b = p
        gc = gcd(x-a, y-b)
        vecto = [(x-a)//gc, (y-b)//gc]
        if vecto[0] in vec_d:
            if vecto[1] in vec_d[vecto[0]]:
                pass
            else:
                vec_d[vecto[0]].add(vecto[1])
                vec_d[-vecto[0]].add(-vecto[1])
        else:
            vec_d[vecto[0]] = {vecto[1]}
            vec_d[-vecto[0]] = {-vecto[1]}

    point.append([x, y])

ans = 0
for key, value in vec_d.items():
    ans += len(value)

print(ans)

        
