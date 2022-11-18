from collections import defaultdict

n, x, y = map(int, input().split())

tree = defaultdict(set)
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].add(b)
    tree[b].add(a)

leaves = [0 for _ in range(n+1)]

step = 1
stack = [x, ]
already = {x, }

while stack:
    stack_ = set()
    for leaf in stack:
        for tar_leaf in tree[leaf]:
            if tar_leaf not in already:
                leaves[tar_leaf] = leaf
                stack_.add(tar_leaf)
                already.add(tar_leaf)

    step += 1
    stack = stack_.copy()

ans_lis = [y, ]
while ans_lis[-1] != x:
    ans_lis.append(leaves[ans_lis[-1]])

ans_lis.reverse()

print(' '.join([str(i) for i in ans_lis]))




