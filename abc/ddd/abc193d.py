k = int(input())
S = list(input())
T = list(input())

str_count = [k]*10
for s in range(10):
    str_count[s] -= S.count(str(s))+T.count(str(s))

count = 0
win_count = 0
for i in range(1, 10):
    if str_count[i] == 0:
        continue
    else:
        S_point = 0
        for si in range(1, 10):
            if si == i:
                S_point += si * (10**(S.count(str(si)) + 1))
            else:
                S_point += si * (10 ** S.count(str(si)))
        case = str_count[i]

        copy_count = str_count.copy()
        copy_count[i] -= 1

        for j in range(1, 10):
            if copy_count[j] == 0:
                continue

            else:
                T_point = 0
                for tj in range(1, 10):
                    if tj == j:
                        T_point += tj * (10**(T.count(str(tj)) + 1))
                    else:
                        T_point += tj * (10**(T.count(str(tj))))

            if S_point > T_point:
                count += case * copy_count[j]
                win_count += case * copy_count[j]
            else:
                count += case * copy_count[j]

print(win_count/count)

