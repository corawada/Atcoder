from collections import deque
from collections import defaultdict
n, m = map(int, input().split())

load = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    load[a].append(b)
    load[b].append(a)

flag = [False] * n
flag[0] = True
stack = deque([[1, load[1]],])
ans_list = [0]*n
ans_list[0] = 1

# print(load)

while stack:
    now_node = stack.popleft()
    for node in now_node[1]:
        if flag[node-1]:
            continue
        else:
            flag[node-1] = True
            stack.append([node, load[node]])
            ans_list[node-1] = now_node[0]

# print(stack)
# print(ans_list)

print('Yes')
for i in ans_list[1:]:
    print(i)





