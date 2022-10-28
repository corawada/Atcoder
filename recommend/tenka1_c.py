from collections import deque
n = int(input())
A = list()
for _ in range(n): A.append(int(input()))
A_que = deque(sorted(A))

pre = A_que.pop()
pre_ans = 0
flag = 1
print(pre)
while A_que:
    if flag:
        pre_ = A_que.popleft()
        pre_ans += pre - pre_
        flag = 0
    else:
        pre_ = A_que.pop()
        pre_ans += pre_ - pre
        flag = 1
    pre = pre_
    print(pre)

ans = pre_ans
print('---', pre_ans)




A_que = deque(sorted(A))
pre = A_que.popleft()
pre_ans = 0
flag = 0
while A_que:
    if flag:
        pre_ = A_que.popleft()
        pre_ans += pre - pre_
        flag = 0
    else:
        pre_ = A_que.pop()
        pre_ans += pre_ - pre
        flag = 1
    pre = pre_

print(max(ans, pre_ans))
print(ans, pre_ans)

