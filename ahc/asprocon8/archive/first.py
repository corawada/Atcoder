S, C, H, a, b = map(int, input().split())
nn = list()
aa = list()
bb = list()
for _ in range(S):
    nn.append(list(map(int, input().split())))
K = list(map(int, input().split()))
for _ in range(S):
    aa.append(list(map(int, input().split())))
for _ in range(C):
    bb.append(list(map(int, input().split())))
# ans_list = list()
ans_list = ['-1' for _ in range(H)]


nn_stack = set()
def add_nn_stack(coor):
    nn_stack.add(coor[0]*C + coor[1])

def jadge_in_nn_stack(coor):
    if coor[0]*C + coor[1] in nn_stack:
        return True
    else:
        return False

def p_to_coor(poi):
    return [poi//C, poi%C]

def coor_to_p(coor):
    return coor[0]*C + coor[1] 

def calc_tt_table(a_table, b_table):
    t_table = list()
    for start in range(S*C):
        coor = p_to_coor(start)
        tmp_list = list()
        for i in range(S):
            for j in range(C):
                tmp_list.append(max(aa[coor[0]][i], bb[coor[1]][j]))
        t_table.append(tmp_list)

    return t_table

tt = calc_tt_table(aa, bb)

# search now point ( != 0 )
flag = False
for idx, raw_nn in enumerate(nn):
    for idy, num in enumerate(raw_nn):
        if num != 0:
            now = [idx, idy]
            flag = True
            break
    if flag:
        break

tt[coor_to_p(now)][coor_to_p(now)] = 1000
conti = True
while conti:
    quantity = nn[now[0]][now[1]]
    hunger = K[now[0]]
    mono = ['{} {}'.format(now[0]+1, now[1]+1) for _ in range(hunger)]

    for _ in range(quantity//hunger):
        ans_list.extend(mono)
        for _ in range(H-hunger):
            if ans_list[-H][0] == '-':
                ans_list.append('-2')
            else:
                ans_list.append('-1')

    if quantity % hunger != 0:
        ans_list.extend(['{} {}'.format(now[0]+1, now[1]+1) for _ in range(quantity%hunger)])
        for _ in range(H-quantity%hunger):
            if ans_list[-H][0] == '-':
                ans_list.append('-2')
            else:
                ans_list.append('-1')


    add_nn_stack(now)

    while True:
        tmp_value = 999
        tmp_id = 1000
        for idx, value in enumerate(tt[coor_to_p(now)]):
            if value < tmp_value:
                tmp_value = value
                tmp_id = idx

        if tmp_id == 1000:
            conti = False
            break
        elif tmp_id in nn_stack:
            tt[coor_to_p(now)][tmp_id] = 1000
            continue
        else:
            tt[coor_to_p(now)][tmp_id] = 1000
            now = p_to_coor(tmp_id)
            for _ in range(tmp_value):
                if ans_list[-H][0] == '-':
                    ans_list.append('-2')
                else:
                    ans_list.append('-1')
            break

print(len(ans_list[250:]))
for ans in ans_list[250:]:
    print(ans)








