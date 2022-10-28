from math import ceil
si, sj, ti, tj, p = input().split()
si, sj, ti, tj = map(int, [si, sj, ti, tj])
p = float(p)

# 縦向きの壁
h_wall = list()
for i in range(20):
    h_wall.append(input())

w_wall = list()
for i in range(19):
    w_wall.append(input())

directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

nn = [[0]*20 for _ in range(20)]
nn[si][sj] = 1
visited = set()
def add_visited(point):
    visited.add(point[0]*19 + point[1])

def jadge_visited(point):
    if point[0]*19 + point[1] in visited:
        return True
    else:
        return False

add_visited([si, sj])

stack = [[si, sj], ]

flag = False
counter = 0
while (stack and (not flag)) and (counter<30):
    counter += 1
    next_stack = []
    for pop_point in stack:
        if pop_point == [ti, tj]:
            flag = True
            break
        # [0, 1] について
        now_point = pop_point.copy()
        for step in range(1, 21):
            if (now_point[1] + 1 == 20) or (h_wall[now_point[0]][now_point[1]]=='1'):
                if jadge_visited(now_point):
                    pass
                else:
                    add_visited(now_point)
                    next_stack.append(now_point)
                    nn[now_point[0]][now_point[1]] = [pop_point[0], pop_point[1], 'R', step]
                break
            elif now_point == [ti, tj]:
                flag = True
                nn[now_point[0]][now_point[1]] = [pop_point[0], pop_point[1], 'R', step]
                break
            else:
                now_point[1] += 1

        # [0, -1] について
        now_point = pop_point.copy()
        for step in range(1, 21):
            if (now_point[1] - 1 == -1) or (h_wall[now_point[0]][now_point[1]-1]=='1'):
                if jadge_visited(now_point):
                    pass
                else:
                    add_visited(now_point)
                    next_stack.append(now_point)
                    nn[now_point[0]][now_point[1]] = [pop_point[0], pop_point[1], 'L', step]
                break
            elif now_point == [ti, tj]:
                nn[now_point[0]][now_point[1]] = [pop_point[0], pop_point[1], 'L', step]
                flag = True
                break
            else:
                now_point[1] -= 1

        # [1, 0] について
        now_point = pop_point.copy()
        for step in range(1, 21):
            if (now_point[0] + 1 == 20) or (w_wall[now_point[0]][now_point[1]]=='1'):
                if jadge_visited(now_point):
                    pass
                else:
                    add_visited(now_point)
                    next_stack.append(now_point)
                    nn[now_point[0]][now_point[1]] = [pop_point[0], pop_point[1], 'D', step]
                break
            elif now_point == [ti, tj]:
                nn[now_point[0]][now_point[1]] = [pop_point[0], pop_point[1], 'D', step]
                flag = True
                break
            else:
                now_point[0] += 1

        # [-1, 0] について
        now_point = pop_point.copy()
        for step in range(1, 21):
            if (now_point[0] - 1 == -1) or (w_wall[now_point[0]-1][now_point[1]]=='1'):
                if jadge_visited(now_point):
                    pass
                else:
                    add_visited(now_point)
                    next_stack.append(now_point)
                    nn[now_point[0]][now_point[1]] = [pop_point[0], pop_point[1], 'U', step]
                break
            elif now_point == [ti, tj]:
                nn[now_point[0]][now_point[1]] = [pop_point[0], pop_point[1], 'U', step]
                flag = True
                break
            else:
                now_point[0] -= 1

    stack = next_stack.copy()


if flag:
    now_point = [ti, tj]
    count = 0
    while not((now_point[0] == si) and (now_point[1] == sj)):
        now_point = nn[now_point[0]][now_point[1]]
        count += now_point[3]

    times = min(ceil(p/0.09), 200//count)
    now_point = [ti, tj]
    root = [now_point, ]
    pre_ans_str = ''
    while not((now_point[0] == si) and (now_point[1] == sj)):
        now_point = nn[now_point[0]][now_point[1]]
        pre_ans_str += now_point[2]*now_point[3] * times
        root.append(now_point)

    print(pre_ans_str[::-1]+pre_ans_str[0]*max(0, 200-len(pre_ans_str)-1))
else:
    print('U')


print(nn[19][19])
