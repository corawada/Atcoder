from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


import math
n = int(input())
sx, sy, tx, ty = map(int, input().split())

circle_list = list()
uf = UnionFind(n)
# uf.union(a, b)
for i in range(n):
    a, b, r = map(int, input().split())
    for idx, cir in enumerate(circle_list):
        d = (cir[0]-a)**2 + (cir[1]-b)**2
        if (r-cir[2])**2 <= d<= (cir[2]+r)**2:
            uf.union(idx, i)

    if math.sqrt((a-sx)**2+(b-sy)**2) == r:
        start_cir = i

    if math.sqrt((a-tx)**2+(b-ty)**2) == r:
        end_cir = i

    circle_list.append([a, b, r])

if end_cir in uf.members(start_cir):
    print('Yes')
else:
    if n == 1:
        print('Yes')
    else:
        print('No')




