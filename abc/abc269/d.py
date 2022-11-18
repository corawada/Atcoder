from collections import defaultdict

class UnionFind():
    # 初期化
    def __init__(self, n):
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


# =============== MAIN ===============

hexagon = dict()
n = int(input())

uf = UnionFind(n)

for i in range(n):
    a, b = map(int, input().split())
    for idx, gon in hexagon.items():
        if (a==gon[0]) and (abs(b-gon[1]) == 1):
            uf.union(i, idx)
        elif (b==gon[1]) and (abs(a-gon[0]) == 1):
            uf.union(i, idx)
        elif (a-gon[0] == b-gon[1] == 1):
            uf.union(i, idx)
        elif (a-gon[0] == b-gon[1] == -1):
            uf.union(i, idx)

    hexagon[i] = [a, b]

print(uf.group_count())


