
## TEMPLATE

# ===== TOOL IMPORT =====
from copy import deepcopy
from collections import defaultdict
import math

class UnionFind():
    def __init__(self, n):
        # 初期化
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        # 親の名前を返す
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

# ===== INPUT =====
n, k = map(int, input().split())
raw_nn = list()
for _ in range(n):
    raw_nn.append(list(input() + '9'))
raw_nn.append(list('9'*(n+1)))

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


# for row in raw_nn:
#     print(row)
# for row in new_nn:
#     print(row)


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


# if len(joint) <= k * 100:
#     print(len(joint))
#     for an in joint:
#         print(' '.join([str(i) for i in an]))
# else:
#     print(k*100)
#     for an in joint[:k*100]:
#         print(' '.join([str(i) for i in an]))





# ===== MAIN 2 =====

# ===== OUTPUT =====


# print(joint)
# print(len(joint))


# ===== SUBMIT =====

