from collections import deque, defaultdict
n = int(input())
S = deque(map(int, input().split()))

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

    # 二つの要素が同じ木にいるか
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # root を返す
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]



uf = UnionFind(2*(10**5)+1)

change_d = dict()
count = 0
for _ in range(n//2):
    l = S.popleft()
    r = S.pop()
    if uf.same(l, r):
        pass
    else:
        uf.union(l, r)
        count += 1

print(count)


