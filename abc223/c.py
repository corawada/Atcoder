N = int(input())

sum_time = 0
douka = list()
for _ in range(N):
    a, b = map(int, input().split())
    douka.append([a, b, a/b])
    sum_time += a/b

sum_time = sum_time/2
how_long = 0
for d in douka:
    if sum_time <= d[2]:
        how_long += sum_time * d[1]
        break
    else:
        how_long += d[0]
        sum_time -= d[2]

print(how_long)


    

