from math import floor
x, m, c, e = map(int, input().split())

for _ in range(m*9):
    input()

const_list = [4 for _ in range(m)]
break_num_list = [0 for _ in range(m)]
for _ in range(e):
    # layer : output
    for i in range(m):
        work_num = 2*(x-break_num_list[i])
        poor_num = 2*break_num_list[i]
        print(str(const_list[i])*work_num + '1'*poor_num)


    # layer : input
    score, v, d = map(int, input().split())

    delay = [0 for _ in range(m)]
    load_count = [[] for _ in range(m)]
    for im in range(m):
        for _ in range(x):
            rd, ro = input().split()
            delay[im] += int(ro)
            load_count[im].append(rd=='0.000')

    for idx, value in enumerate(delay):
        if value:
            if const_list[idx] != 9:
                const_list[idx] += 1

    if score != 0:
        for idx, bool_list in enumerate(load_count):
            cnt = 0
            while bool_list:
                if bool_list.pop() == True:
                    cnt += 1
                else:
                    break
            break_num_list[idx] = max(break_num_list[idx], cnt)








