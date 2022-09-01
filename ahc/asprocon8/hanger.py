S, C, H, a, b = map(int, input().split())
nn = list()
aa = list()
bb = list()
for _ in range(S):
    nn.append(list(map(int, input().split())))
hunger_dic = {key:int(value) for key, value in zip(range(S), input().split())}
for _ in range(S):
    aa.append(list(map(int, input().split())))
for _ in range(C):
    bb.append(list(map(int, input().split())))
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

def cool_time_append(num):
    for _ in range(num):
        folm = int(ans_list[-H].split()[0])
        if folm < 0:
            ans_list.append('-2 0')
        else:
            hunger_dic[folm-1] += 1
            ans_list.append('-1 0')

def collect_hunger():
    folm = int(ans_list[-H].split()[0])
    if folm < 0:
        return False
    else:
        hunger_dic[folm-1] += 1
        return True

def calc_fill_blank_pruduct(coor, blank):
    tmp_max_blank = 0
    return_coor = list()
    for idx, value in enumerate(tt[coor_to_p(coor)]):
        tar_coor = p_to_coor(idx)
        tmp = value + nn[tar_coor[0]][tar_coor[1]] + tt[idx][coor_to_p(coor)]
        if tmp_max_blank < tmp <= blank:
            tmp_max_blank = max(tmp_max_blank, tmp)
            return_coor = tar_coor

    return return_coor

tt = calc_tt_table(aa, bb)

print(S)
print(aa)









