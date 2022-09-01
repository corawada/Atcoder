# 基本方針
# 移動はしないで、直線同士で結べるノードのみ結ぶ
# 長い直線が発生しないように、閾値を設ける

# update +++ fifth: 隣接するlineに吸収される

# ===== INIT =====
from collections import defaultdict
from copy import deepcopy

class UnionFind():
    def __init__(self, n):
        # 初期化
        self.n = n; self.parents = [-1] * n
    # 親の名前を返す
    def find(self, x):
        # 親の名前を返す
        if self.parents[x] < 0: return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    # 結合
    def union(self, x, y):
        x = self.find(x); y = self.find(y)
        if x == y: return
        if self.parents[x] > self.parents[y]: x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    # 結合している数を返す
    def size(self, x): return -self.parents[self.find(x)]
    # 二つの要素が同じ木にいるか
    def same(self, x, y): return self.find(x) == self.find(y)
    # 同じ木にいるmemberをリストで返す
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    # root を返す
    def roots(self): return [i for i, x in enumerate(self.parents) if x < 0]
    # groupの数をかえす
    def group_count(self): return len(self.roots())
    # 全てのgroupのmemberを辞書形式で返す
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members
    def __str__(self): return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


def jadge_cell_type(array, i, j):
    # return ==> 0 : 内容なし（０）
    #        ==> 1 : 内容あり（int）
    #        ==> 2 : line  ([num, id, id], [num, zahyo, zahyo)
    #        ==> 3 : 入力不可
    cell = array[i][j]
    if len(cell) == 1:
        if cell == '9':
            return [3, 0, 0]
        elif cell == '0':
            return [0, 0, 0]
        else:
            return [1, int(cell), 0]
    else:
        num, line_num = int(cell[1]), int(cell[2:])
        xi, xj, yi, yj = joint[line_num]
        x_z = xi * n + xj
        y_z = yi * n + yj
        return [2, [num, point_dict[num][x_z], point_dict[num][y_z]], \
                [num, x_z, y_z]]


# ===== INPUT =====
n, k = map(int, input().split())
raw_nn = [list(input()+'9') for _ in range(n)]
raw_nn.append(list('9'*(n+1)))

trans = list()
joint = list()

# ===== PREPROCESSING =====
nn = deepcopy(raw_nn)

point_dict_ = [[] for _ in range(k)]

for i in range(n):
    for j in range(n):
        point = nn[i][j]
        if point != '0':
            point_dict_[int(point)-1].append(n*i + j)
# point_dict[s][t] でnum==s かつt=point のidを取得
# rev_point_dict[s][t] でnum==s かつt=id のpointを取得
point_dict = [0, ]
rev_point_dict = [0, ]
for cp_num in point_dict_:
    tmp_dic = dict()
    tmp_rev_dic = dict()
    for idx, p in enumerate(cp_num):
        tmp_dic[p] = idx
        tmp_rev_dic[idx] = p
    point_dict.append(tmp_dic)
    rev_point_dict.append(tmp_rev_dic)

# print(point_dict)

# ===== MAIN 1 =====
# 大まかにつなげる
uf_cp = [UnionFind(100) for _ in range(k+1)]
line_num = 0
for iki in range(1, n):
    for i in range(n):
        for j in range(n):
            now_point = int(nn[i][j])
            if not (1 <= now_point <= k):
                continue

            for si in range(1, iki+1):
                tar_point = int(nn[i+si][j][0])
                if tar_point  == 0:
                    continue
                elif tar_point == 9:
                    break
                else:
                    if (si == iki) and (tar_point == now_point):
                        if not uf_cp[now_point].same(point_dict[now_point][n*i+j], \
                                point_dict[now_point][n*(i+iki)+j]):
                            for si_i in range(1, iki):
                                nn[i+si_i][j] = '9' + str(now_point) + str(line_num)
                                
                            line_num += 1
                            joint.append([i, j, i+iki, j])
                            uf_cp[now_point].union(point_dict[now_point][n*i+j], \
                                    point_dict[now_point][n*(i+iki)+j])
                    break

            for sj in range(1, iki+1):
                tar_point = int(nn[i][j+sj])
                if tar_point  == 0:
                    continue
                elif tar_point == 9:
                    break
                else:
                    if (sj == iki) and (tar_point == now_point):
                        if not uf_cp[now_point].same(point_dict[now_point][n*i+j], \
                                point_dict[now_point][n*i+j+iki]):
                            for sj_j in range(1, iki):
                                nn[i][j+sj_j] = '9' + str(now_point) + str(line_num)
                                
                            line_num += 1
                            joint.append([i, j, i, j+iki])
                            uf_cp[now_point].union(point_dict[now_point][n*i+j], \
                                    point_dict[now_point][n*i+j+iki])
                    break

# ===== MAIN 2 =====
# 隣接するlineがあれば接続する
#TODO: now
del_point = list()
add_point = list()
trans_nums = list() # trans と対応
for num in range(1, k+1): # どの番号についてか
    for p_id in range(0, 100):
        tar_point_ = rev_point_dict[num][p_id]
        tar_point = [tar_point_//n, tar_point_%n]
        ue = jadge_cell_type(nn, tar_point[0] - 1, tar_point[1])
        si = jadge_cell_type(nn, tar_point[0] + 1, tar_point[1])
        mi = jadge_cell_type(nn, tar_point[0] , tar_point[1] + 1)
        hi = jadge_cell_type(nn, tar_point[0] , tar_point[1] - 1)











# ===== MAIN 3 =====
new_nn = deepcopy(raw_nn)

for num, tra in zip(trans_nums, trans):
    new_nn[tra[0]][tra[1]] = '0'
    new_nn[tra[2]][tra[3]] = str(num)

point_dict_ = [[] for _ in range(k)]
for i in range(n):
    for j in range(n):
        point = new_nn[i][j]
        if point != '0':
            point_dict_[int(point)-1].append(n*i + j)
point_dict = [0, ]
rev_point_dict = [0, ]
for cp_num in point_dict_:
    tmp_dic = dict()
    tmp_rev_dic = dict()
    for idx, p in enumerate(cp_num):
        tmp_dic[p] = idx
        tmp_rev_dic[idx] = p
    point_dict.append(tmp_dic)
    rev_point_dict.append(tmp_rev_dic)

uf_cp = [UnionFind(100) for _ in range(k+1)]
line_num = 0
joint = list()
for iki in range(1, n):
    for i in range(n):
        for j in range(n):
            now_point = int(new_nn[i][j])
            if not (1 <= now_point <= k):
                continue

            for si in range(1, iki+1):
                tar_point = int(new_nn[i+si][j][0])
                if tar_point  == 0:
                    continue
                elif tar_point == 9:
                    break
                else:
                    if (si == iki) and (tar_point == now_point):
                        if not uf_cp[now_point].same(point_dict[now_point][n*i+j], \
                                point_dict[now_point][n*(i+iki)+j]):
                            for si_i in range(1, iki):
                                new_nn[i+si_i][j] = '9' + str(now_point) + str(line_num)
                                
                            line_num += 1
                            joint.append([i, j, i+iki, j])
                            uf_cp[now_point].union(point_dict[now_point][n*i+j], \
                                    point_dict[now_point][n*(i+iki)+j])
                    break

            for sj in range(1, iki+1):
                tar_point = int(new_nn[i][j+sj])
                if tar_point  == 0:
                    continue
                elif tar_point == 9:
                    break
                else:
                    if (sj == iki) and (tar_point == now_point):
                        if not uf_cp[now_point].same(point_dict[now_point][n*i+j], \
                                point_dict[now_point][n*i+j+iki]):
                            for sj_j in range(1, iki):
                                new_nn[i][j+sj_j] = '9' + str(now_point) + str(line_num)
                                
                            line_num += 1
                            joint.append([i, j, i, j+iki])
                            uf_cp[now_point].union(point_dict[now_point][n*i+j], \
                                    point_dict[now_point][n*i+j+iki])
                    break
# ===== SUBMIT =====

# cnt = 0
# print(len(trans))
# for tra in trans:
#     print(tra[0], tra[1], tra[2], tra[3])
#     cnt += 1
#
# print(min(len(joint), k*100 - len(trans)))
# for joi in joint:
#     if cnt == k * 100:
#         break
#     print(joi[0], joi[1], joi[2], joi[3])
#     cnt += 1
#
