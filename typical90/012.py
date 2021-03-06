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

h, w = map(int, input().split())
q = int(input())

uf = UnionFind(h*w)

red_point = set()
for _ in range(q):
    a, y1, x1, *c = map(int, input().split())
    if a == 1:
        red_point.add((y1-1)*w+x1-1)
        for sy, sx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            tar = (y1+sy-1)*w+x1+sx-1 
            if tar in red_point:
                if [y1+sy, x1+sx] == [(tar//w)+1, tar%w+1]:
                    uf.union((y1-1)*w+x1-1, (y1+sy-1)*w+x1+sx-1)
    else:
        y2, x2 = c
        if (uf.same((y1-1)*w+x1-1, (y2-1)*w+x2-1)) and ((y1-1)*w+x1-1 in red_point):
            print('Yes')
        else:
            print('No')

