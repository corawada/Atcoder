from math import ceil, floor
from bisect import bisect_left
from copy import deepcopy
from itertools import combinations

patern_time_ = [-1, 0, 3, 5, 8, 10, 12, 14, 16, 18]
patern_time = [i*3600*7 for i in patern_time_]

x, m, c, e = map(int, input().split())
for _ in range(m*9):
    input()
## first step すべてのマシンの時間を測る
tmp_ans = '9'*(2*x)
for i in range(m):
    print(tmp_ans)

sum_rate_for_machine = []
input()
for im in range(m):
    ratio = 0.0
    for _ in range(x):
        rd, ro = input().split()
        ratio += float(rd)
    sum_rate_for_machine.append(ratio)

const_sum_time_for_machine = [ceil(i*64800*7) for i in sum_rate_for_machine]
remain_time_for_machine = const_sum_time_for_machine.copy()

# 平均化されたansを算出
const_list = []
for m_time in const_sum_time_for_machine:
    idx = bisect_left(patern_time, ceil(m_time/x))
    const_list.append(idx)

ans_list = list()
for pat in const_list:
    tmp_list = [pat, ]
    tmp_list.extend([9 for _ in range(x-1)])
    ans_list.append(tmp_list)


# second step Cを気にせず最小のansを作成する
# fase 1
counter = 1
target_week = 0
pre_delay = [[0]*x for _ in range(m)]

while counter != e:
    counter += 1
    for week_machine in ans_list:
        ans_str = ''
        for tar in week_machine:
            ans_str += str(tar)*2
        print(ans_str)

    score, v, d = map(int, input().split())
    delay = []
    load_rate = []
    for im in range(m):
        del_li = []
        loa_li = []
        for _ in range(x):
            rd, ro = input().split()
            del_li.append(int(ro))
            loa_li.append(ceil(float(rd)*100))
        delay.append(del_li)
        load_rate.append(loa_li)

    flag = True
    up_flag = [False for _ in range(m)]
    this_delay = 0
    for machine in range(m):
        this_delay += delay[machine][target_week]
        if delay[machine][target_week] == 0:
            # 稼働率から、もしansを減らせるなら減らす
            kadou_time = ceil(patern_time[ans_list[machine][target_week]] * \
                    load_rate[machine][target_week])
            if kadou_time <= patern_time[ans_list[machine][target_week] -1]:
                ans_list[machine][target_week] -= 1
                flag = False
            else:
                pass
        elif ans_list[machine][target_week] == 9:
            pass
        elif delay[machine][target_week] == pre_delay[machine][target_week]:
            # 同じ週のloadrateが100のmachineを1上げる
            # ans_list[machine][target_week] -= 1
            delay[machine][target_week] = 10**5
            for tar_mac in range(m):
                if load_rate[tar_mac][target_week] > 90:
                    if up_flag[tar_mac] or (ans_list[tar_mac][target_week]==9):
                        continue
                    else:
                        ans_list[tar_mac][target_week] += 1
                        up_flag[tar_mac] = True
            flag = False
        else:
            ans_list[machine][target_week] += 1
            flag = False

    if flag and (target_week != x-1): # やることがなくなった
        if this_delay != 0: # 前の週に戻ってやり直し
            for machine_num in range(m):
                if pre_load_rate[machine_num][target_week-1] > 90:
                    if ans_list[machine_num][target_week-1] == 9:
                        pass
                    else:
                        ans_list[machine_num][target_week-1] += 1
                ans_list[machine_num][target_week] = 9
            target_week -= 1

        else:
            for i, value in enumerate(const_list):
                ans_list[i][target_week+1] = value

            
            target_week += 1
            delay = [[0]*x for _ in range(m)]
    elif flag and (target_week == x-1):
        pre_delay = deepcopy(delay)
        pre_load_rate = deepcopy(load_rate)
        break

    # end loop
    pre_delay = deepcopy(delay)
    pre_load_rate = deepcopy(load_rate)

# patern_time_ = [-1, 0, 3, 5, 8, 10, 12, 14, 16, 18]
# 作られたansからCの数に見合ったものを作る
re_patern_dic = dict()
for i, value in enumerate(patern_time_):
    re_patern_dic[value] = i

def create_min_sol(input_lis, C):
    tar_lis = [patern_time_[i] for i in input_lis]
    len_a = len(tar_lis)
    tmp_ans_lis = [[max(tar_lis) for _ in range(len_a)], ]
    tmp_max_sum = sum(tmp_ans_lis[0])

    for i in range(len_a):
        tmp_list = [max(tar_lis[:i+1]) for _ in range(i+1)] + \
                [max(tar_lis[i+1:]) for _ in range(len_a - i -1)]
        if tmp_max_sum > sum(tmp_list):
            tmp_max_sum = sum(tmp_list)
            tmp_ans_lis = [tmp_list, ]
        elif tmp_max_sum == sum(tmp_list):
            tmp_ans_lis.append(tmp_list)
    if C >= 4:
        for a, b,  in combinations(range(len_a), 2):
            tmp_list = [max(tar_lis[:a+1]) for _ in range(a+1)] + \
                    [max(tar_lis[a+1:b+1]) for _ in range(b-a)] + \
                    [max(tar_lis[b+1:]) for _ in range(len_a - b - 1)]
            if tmp_max_sum > sum(tmp_list):
                tmp_max_sum = sum(tmp_list)
                tmp_ans_lis = [tmp_list, ]
            elif tmp_max_sum == sum(tmp_list):
                tmp_ans_lis.append(tmp_list)

    if C >= 6:
        for a, b, c in combinations(range(len_a), 3):
            tmp_list = [max(tar_lis[:a+1]) for _ in range(a+1)] + \
                    [max(tar_lis[a+1:b+1]) for _ in range(b-a)] + \
                    [max(tar_lis[b+1:c+1]) for _ in range(c-b)] + \
                    [max(tar_lis[c+1:]) for _ in range(len_a - c - 1)]
            if tmp_max_sum > sum(tmp_list):
                tmp_max_sum = sum(tmp_list)
                tmp_ans_lis = [tmp_list, ]
            elif tmp_max_sum == sum(tmp_list):
                tmp_ans_lis.append(tmp_list)

    if C >= 8:
        for a, b, c, d in combinations(range(len_a), 4):
            tmp_list = [max(tar_lis[:a+1]) for _ in range(a+1)] + \
                    [max(tar_lis[a+1:b+1]) for _ in range(b-a)] + \
                    [max(tar_lis[b+1:c+1]) for _ in range(c-b)] + \
                    [max(tar_lis[c+1:d+1]) for _ in range(d-c)] + \
                    [max(tar_lis[d+1:]) for _ in range(len_a - d - 1)]
            if tmp_max_sum > sum(tmp_list):
                tmp_max_sum = sum(tmp_list)
                tmp_ans_lis = [tmp_list, ]
            elif tmp_max_sum == sum(tmp_list):
                tmp_ans_lis.append(tmp_list)

    return_lis = [re_patern_dic[i] for i in tmp_ans_lis[0]]
    return return_lis


small_ans_list = deepcopy(ans_list)
ans_list = []
for tmp_ans in small_ans_list:
    return_lis = create_min_sol(tmp_ans, c)
    ans_list.append(return_lis)
# print(small_ans_list)
# print(ans_list)

# faze 2
while counter != e:
    counter += 1
    for week_machine in ans_list:
        ans_str = ''
        for tar in week_machine:
            ans_str += str(tar)*2
        print(ans_str)

    score, v, d = map(int, input().split())
    delay = []
    load_rate = []
    for im in range(m):
        del_li = []
        loa_li = []
        for _ in range(x):
            rd, ro = input().split()
            del_li.append(int(ro))
            loa_li.append(ceil(float(rd)*100))
        delay.append(del_li)
        load_rate.append(loa_li)

# print(ans_list)

