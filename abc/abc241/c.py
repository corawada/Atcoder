from collections import deque

n = int(input())

nn = deque()
ll = [deque() for _ in range(n)]

# 横
flag = False
for i in range(n):

    sn = deque(input())
    nn.append(sn.copy())

    six_que = deque()
    for j in range(6):
        val = sn.popleft()
        six_que.append(val)
        ll[j].append(val)
    if six_que.count('#') >= 4:
        flag = True
        break

    for j in range(6, n):
        val = sn.popleft()
        six_que.popleft()
        six_que.append(val)
        ll[j].append(val)
        if six_que.count('#') >= 4:
            flag = True
            break

    if flag:
        break

# 縦
ll = deque(ll)
for i in range(n):
    ln = ll.popleft()
    six_que = deque()
    for j in range(6):
        six_que.append(ln.popleft())
    if six_que.count('#') >= 4:
        flag = True
        break

    for j in range(6, n):
        six_que.popleft()
        six_que.append(ln.popleft())
        if six_que.count('#') >= 4:
            flag = True
            break

if flag:
    print("Yes")

        




