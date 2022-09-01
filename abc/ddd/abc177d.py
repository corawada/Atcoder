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


    # 全てのgroupのmemberを辞書形式で返す
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

n, m = map(int, input().split())
uf = UnionFind(n)
for _ in range(m):
    a, b = map(int, input().split())
    uf.union(a-1, b-1)

ans = 0
for union in uf.all_group_members().values():
    ans = max(ans, len(union))

print(ans)

