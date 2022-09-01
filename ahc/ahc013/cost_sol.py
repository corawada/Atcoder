# ===== TOOL IMPORT =====
import math
from collections import defaultdict
from pprint import pprint
from copy import deepcopy

direction4 = [[-1, 0], [1, 0], [0, -1], [0, 1]]

class UnionFind():
    def __init__(self, n):
    # 初期化
        self.n = n
        self.parents = [-1] * n

    # 親の名前を返す
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # 結合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    # 結合している数を返す
    def size(self, x):
        return -self.parents[self.find(x)]

    # 二つの要素が同じ木にいるか
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # 同じ木にいるmemberをリストで返す
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    # root を返す
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    # groupの数をかえす
    def group_count(self):
        return len(self.roots())

    # 全てのgroupのmemberを辞書形式で返す
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

def point_to_id(i, j):
    return i*n + j

def id_to_point(idx):
    return (idx//n, idx%n)

def calc_point(x):
    return (x*(x-1)) // 2

# ===== INPUT =====
n, k = map(int, input().split())
raw_nn = [list(input()+'9') for _ in range(n)]
raw_nn.append(list('9'*(n+1)))

# ===== PROPROCESSING =====
reach = math.ceil((n**2)//(50*k))

def update_con_bene_nn(nn):
    # 全てのセルのcostを計算する準備をする
    benefit_nn = [[[list() for _ in range(k+1)] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            now_point = int(nn[i][j])

            for direction in direction4:
                for step in range(1, reach+1):
                    tar_coor = [i+step*direction[0], j+step*direction[1]]
                    step_point = int(nn[tar_coor[0]][tar_coor[1]])
                    if step_point == 0:
                        continue
                    elif step_point == 9:
                        break
                    else:
                        benefit_nn[i][j][step_point].append(point_to_id(tar_coor[0], tar_coor[1]))

    return benefit_nn

def calc_cost_nn(bene_nn, union):
    cost_nn = [[[0]*(k+1) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            conections = bene_nn[i][j]
            for num, conn in enumerate(conections):
                tree_root = set()
                for con in conn:
                    tree_root.add(union[num].find(re_coor[num][con]))
                tmp_cost = 0
                for ids in tree_root:
                    tmp_cost += calc_point(union[num].size(ids))

                cost_nn[i][j][num] += tmp_cost

    return cost_nn

def search_and_connect(nn):
    tmp_nn = deepcopy(nn)
    uf = [0, ]
    coordinates = [0, ]
    re_coor = [0, ]
    for _ in range(k):
        uf.append(UnionFind(100))
        coordinates.append(list())
        re_coor.append(dict())
    for i in range(n):
        for j in range(n):
            point = int(tmp_nn[i][j])
            if point != 0:
                re_coor[point][point_to_id(i, j)] = len(coordinates[point]) 
                coordinates[point].append(point_to_id(i, j))

    tmp_joint = list()
    for i in range(n):
        for j in range(n):
            point = int(tmp_nn[i][j])
            if (point == 0) or (point == 9):
                continue
            else:
                for di in [[1, 0], [0, 1]]:
                    for step in range(1, reach+1):
                        tar_point = int(tmp_nn[i+step*di[0]][j+step*di[1]])
                        if tar_point == 0:
                            continue
                        elif tar_point != point:
                            break
                        elif tar_point == point:
                            now_id = re_coor[point][point_to_id(i, j)]
                            tar_id = re_coor[point][point_to_id(i+step*di[0], j+step*di[1])]
                            if uf[point].same(now_id, tar_id):
                                continue
                            tmp_joint.append([i, j, i+step*di[0] , j+step*di[1]])
                            uf[point].union(now_id, tar_id)
                            for tc in range(1, step):
                                tmp_nn[i+tc*di[0]][j+tc*di[1]] = '9'
                            break

    return uf, tmp_joint, coordinates, re_coor, tmp_nn

def absorption(nn, cost_nn):
    not_empty_cell = list()
    tmp_move = list()
    for num in range(1, k+1):
        for ids in range(100):
            i, j = id_to_point(coor[num][ids])
            now_cost = cost_nn[i][j][num]
            better_cost = now_cost
            best_direc = 0
            pre_cost = 10**5
            for direc in direction4:
                za = [i+direc[0], j+direc[1]]
                if za in not_empty_cell:
                    continue
                max_direc = 0
                if int(nn[za[0]][za[1]]) == 9:
                    continue
                if (nn[za[0]][za[1]] == '0') and \
                        (cost_nn[za[0]][za[1]][num] == max(cost_nn[za[0]][za[1]])):
                    if cost_nn[za[0]][za[1]][num] > better_cost:
                        best_direc = za
                        if (0<=za[0]+direc[0]<=n-1) and (0<=za[1]+direc[1]<=n-1):
                            pre_cost = cost_nn[za[0]+direc[0]][za[1]+direc[1]][num]
                        else:
                            continue
                    elif cost_nn[za[0]][za[1]][num] == better_cost:
                        if (0<=za[0]+direc[0]<=n-1) and (0<=za[1]+direc[1]<=n-1):
                            next_cost = cost_nn[za[0]+direc[0]][za[1]+direc[1]][num]
                            if pre_cost < next_cost:
                                pre_cost = next_cost
                                best_direc = za
                        else:
                            best_direc = za
            else:
                if best_direc != 0:
                    tmp_move.append([i, j, best_direc[0], best_direc[1]])
                    not_empty_cell.append(best_direc)
    return tmp_move

def move_for_nn(nn, j_lis):
    new_nn = deepcopy(nn)
    for a, b, c, d in j_lis:
        new_nn[c][d] = new_nn[a][b]
        new_nn[a][b] = '0'
    return new_nn

def cut_short_connect(nn, move_l, uf, ikiti):
    new_move_l = deepcopy(move_l)
    
    for a, b, c, d in move_l:
        tar_num = int(nn[c][d])
        tar_num_id = re_coor[tar_num][point_to_id(c, d)]
        if uf[tar_num].size(tar_num_id) == ikiti:
            if nn[a][b] == '0':
                new_move_l.remove([a, b, c, d])

        # try:
        #     tar_num_id = re_coor[tar_num][point_to_id(c, d)]
        #     if uf[tar_num].size(tar_num_id) == ikiti:
        #         if nn[a][b] == '0':
        #             new_move_l.remove([a, b, c, d])
        # except:
        #     continue

    return new_move_l


if k <= 3:
    trans = list()
    if k == 2:
        for i in range(n):
            for j in range(n):
                if (raw_nn[i][j] == '1') and (i%2==0) and (j%2==0):
                    for si, sj in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
                        if raw_nn[i+si][j+sj] == '0':
                            raw_nn[i+si][j+sj] = raw_nn[i][j]
                            raw_nn[i][j] = '0'
                            trans.append([i, j, i+si, j+sj])
                            break
                elif (raw_nn[i][j] == '2') and (i%2==1) and (j%2==1):
                    for si, sj in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
                        if raw_nn[i+si][j+sj] == '0':
                            raw_nn[i+si][j+sj] = raw_nn[i][j]
                            raw_nn[i][j] = '0'
                            trans.append([i, j, i+si, j+sj])
                            break
# ===== PROPROCESSING =====
    joint = list()

# ===== MAIN 1 =====

# 各セルから一番近いnum をlistに反映する
# near_nn ... [bool, [up, do, le, ri]] 
# 2/dence = 閾値としてそれ以上は無視

    near_boder = math.ceil((2 * (n**2)) / (100*k) )
    near_nn = [[[1, []]]*(n+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            # 上を探す
            temp = [9, 9, 9, 9]
            temp_len = [100, 100, 100, 100]
            for step in range(1, min(near_boder, i+1)):
                tar = int(raw_nn[i-step][j])
                if tar == 0:
                    continue
                elif tar == 9:
                    temp[0] = 9
                    break
                else:
                    temp[0] = tar
                    temp_len[0] = step
                    break

            # 下を探す
            for step in range(1, min(near_boder, n-i)):
                tar = int(raw_nn[i+step][j])
                if tar == 0:
                    continue
                elif tar == 9:
                    temp[1] = 9
                    break
                else:
                    temp[1] = tar
                    temp_len[1] = step
                    break

            # 左を探す
            for step in range(1, min(near_boder, j+1)):
                tar = int(raw_nn[i][j-step])
                if tar == 0:
                    continue
                elif tar == 9:
                    temp[2] = 9
                    break
                else:
                    temp[2] = tar
                    temp_len[2] = step
                    break

            # 右を探す
            for step in range(1, min(near_boder, n-j)):
                tar = int(raw_nn[i][j+step])
                if tar == 0:
                    continue
                elif tar == 9:
                    temp[3] = 9
                    break
                else:
                    temp[3] = tar
                    temp_len[3] = step
                    break

            if raw_nn[i][j] == '0':
                near_nn[i][j] = [0, temp, temp_len]
            else:
                near_nn[i][j] = [1, temp, temp_len]


# 移動させるか否かを決定する
    term_trans = list()
    for i in range(n):
        for j in range(n):
            point = int(raw_nn[i][j])
            if point in near_nn[i][j][1]:
                pass
            else:
                move = 0
                move_len = 100

                for idx, ss in enumerate([[-1, 0], [1, 0], [0, -1], [0, 1]]):
                    if (0 <= i+ss[0] < n) and (0 <= j+ss[1] < n):
                        target = near_nn[i+ss[0]][j+ss[1]]
                        if target[0] == 0:
                            for idd, near_ in enumerate(zip(target[1], target[2])):
                                if ((idx//2)*2 + 1 - (idx%2)) == idd:
                                    continue
                                if (point == near_[0]) and (move_len > near_[1]):
                                    move = ss
                            if target[1][0] == target[1][1] == point:
                                move = ss
                                break
                            elif target[1][2] == target[1][3] == point:
                                move = ss
                                break

                if move != 0:
                    trans.append([i, j, i+move[0], j+move[1]])
                    term_trans.append([i, j, i+move[0], j+move[1]])
                    near_nn[i+move[0]][j+move[1]][0] = 1


    new_nn = list()
    for row in raw_nn:
        new_nn.append(list(row))
    for i, j, ni, nj in term_trans:
        new_nn[ni][nj] = new_nn[i][j]
        new_nn[i][j] = '0'


    joint = list()
    for iki in range(1, n+1):
        for i in range(n):
            for j in range(n):
                point = new_nn[i][j]
                if (point == '0') or (point == '9'):
                    continue

                # 下に探す
                for si in range(1, iki+1):
                    if new_nn[i+si][j] == '0':
                        continue
                    else:
                        if (si == iki) and (new_nn[i+si][j] == point):
                            joint.append([i, j, i+si, j])

                            for hi in range(i+1, i+si):
                                new_nn[hi][j] = '9'
                        
                        break

                # 右に探す
                for sj in range(1, iki+1):
                    if new_nn[i][j+sj] == '0':
                        continue
                    else:
                        if (sj == iki) and (new_nn[i][j+sj] == point):
                            joint.append([i, j, i, j+sj])

                            for hj in range(j+1, j+sj):
                                new_nn[i][hj] = '9'
                        
                        break

# ===== SUBMIT =====
    print(len(trans))
    for a, b, c, d in trans:
        print(a, b, c, d)
    joint_print_len = min(len(joint),k*100-len(trans))
    print(joint_print_len)
    for idx in range(joint_print_len):
        a, b, c, d = joint[idx]
        print(a, b, c, d)

        pass
else:
    benefit_nn = update_con_bene_nn(raw_nn)
    uf, joint, coor, re_coor, foot_nn = search_and_connect(raw_nn)

    cost_nn = calc_cost_nn(benefit_nn, uf)
    pre_move = absorption(raw_nn, cost_nn)
    next_nn = move_for_nn(raw_nn, pre_move)
    uf, joint, coor, re_coor, foot_nn = search_and_connect(next_nn)


    # for iki in range(1, 10):
    #     pre_move = cut_short_connect(foot_nn, pre_move, uf, iki)
    #     next_nn = move_for_nn(raw_nn, pre_move)
    #     uf, joint, coor, re_coor, foot_nn = search_and_connect(next_nn)
    #     if k**100 >= len(pre_move) + len(joint):
    #         break

    print(len(pre_move))
    for a, b, c, d in pre_move:
        print(a, b, c, d)


    print(min(k*100-len(pre_move), len(joint)))
    for a, b, c, d in joint[:min(k*100-len(pre_move), len(joint))]:
        print(a, b, c, d)

# ===== MAIN 1 =====



# ===== MAIN 2 =====

# ===== OUTPUT =====
