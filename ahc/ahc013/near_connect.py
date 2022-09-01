# ===== TOOL IMPORT =====
import math
from collections import defaultdict
from pprint import pprint
from copy import deepcopy

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

def point_to_coor(i, j):
    return i*n + j

def coor_to_point(idx):
    return (idx//n, idx%n)

def calc_point(x):
    return (x*(x-1)) // 2

# ===== INPUT =====
n, k = map(int, input().split())
raw_nn = [list(input()+'9') for _ in range(n)]
raw_nn.append(list('9'*(n+1)))
reach = math.ceil((n**2)//(50*k))

# ===== PROPROCESSING =====
def move_for_nn(nn, j_lis):
    new_nn = deepcopy(nn)
    for a, b, c, d in j_lis:
        new_nn[c][d] = new_nn[a][b]
        new_nn[a][b] = '0'
    return new_nn

def search_and_connect(nn, coordinates, re_coor):
    # =>  uf, tmp_joint, tmp_nn
    tmp_nn = deepcopy(nn)
    uf = [0, ]
    for _ in range(k):
        uf.append(UnionFind(100))

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
                            now_id = re_coor[point][point_to_coor(i, j)]
                            tar_id = re_coor[point][point_to_coor(i+step*di[0], j+step*di[1])]
                            if uf[point].same(now_id, tar_id):
                                continue
                            tmp_joint.append([i, j, i+step*di[0] , j+step*di[1]])
                            uf[point].union(now_id, tar_id)
                            for tc in range(1, step):
                                tmp_nn[i+tc*di[0]][j+tc*di[1]] = '9'
                            break
    return uf, tmp_joint, tmp_nn

def reflesh_coordinates(nn):
    # => coordinates, re_coor
    coordinates = [0, ]
    re_coor = [0, ]
    for _ in range(k):
        coordinates.append(list())
        re_coor.append(dict())
    for i in range(n):
        for j in range(n):
            point = int(nn[i][j])
            if point != 0:
                re_coor[point][point_to_coor(i, j)] = len(coordinates[point]) 
                coordinates[point].append(point_to_coor(i, j))
    
    return coordinates, re_coor

def cut_short_connections():
    pass
# ===== MAIN 1 =====

# faze 1 --- 適当に繋ぐ
coor, re_coor = reflesh_coordinates(raw_nn)
uf, joint, _ = search_and_connect(raw_nn, coor, re_coor) 


# ===== MAIN 2 =====

# ===== OUTPUT =====
print(0)
print(len(joint))
for a, b, c, d in joint:
    print(a, b, c, d)
