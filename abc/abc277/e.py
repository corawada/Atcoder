from collections import defaultdict
n, m, k = map(int, input().split())

load_t = defaultdict(set)
load_f = defaultdict(set)

for _ in range(n):
    va, vb, b = map(int, input().split())
    if b:
        load_t[va].add(vb)
        load_t[vb].add(va)
    else:
        load_f[va].add(vb)
        load_f[vb].add(va)

print(load_t)
print(load_f)

already_t = {1, }
already_f = set()

stack = [1, ]

step = 1
flag = True
while stack and flag:
    print(stack)
    # init
    stack_ = list()

    if step % 2 == 1: # true の道
        for var in stack:
            if var == n:
                flag = False
                break
            elif var in load_t:
                for load in load_t[var]:
                    if load not in already_f:
                        already_f.add(load)
                        stack_.append(load)

    else:
        for var in stack:
            if var == n:
                flag = False
                break
            elif var in load_f:
                for load in load_f[var]:
                    if load not in already_t:
                        already_t.add(load)
                        stack_.append(load)

    # end
    step += 1
    stack = stack_.copy()

if flag:
    print(-1)
else:
    print(step-1)
