from time import sleep

a, n = map(int, input().split())

ans = 10**5

que = {n, }
cool = 0
ans = 10000
all_set = que
while True:
    next_que = set()
    for q in que:
        if q == 1:
            ans = min(ans, cool)

        if q % a == 0:
            next_que.add(q//a)

        if (q // 10 == 0) or (q % 10 == 0):
            continue
        else:
            q = str(q)[1:]+str(q)[0]
            if q[0] == '0':
                pass
            else:
                q = int(q)
                if q not in all_set:
                    next_que.add(q)

    que = next_que
    cool += 1
    all_set |= que
    if que == set():
        break
    # print(que, cool)


if ans == 10000:
    print(-1)
else:
    print(ans)


    
