from itertools import combinations
c = 6
A = [3, 2, 2, 4, 2, 3, 2, 2, 2, 2, 2, 2]
print(len(A))


patern_time_ = [-1, 0, 3, 5, 8, 10, 12, 14, 16, 18]
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

print(A)
print(create_min_sol(A, 4))


