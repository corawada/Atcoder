from collections import deque
S = input()
l = len(S)

ans = deque('R')

inv = 0
flag = False
for s in S:
    if s == 'R':
        inv = 1 - inv/1
        continue
    
    if not ans:
        ans.append('R')
        flag = False

    if inv:
        pre = ans.popleft()
        if pre != s:
            ans.appendleft(pre)
            ans.appendleft(s)
    else:
        pre = ans.pop()
        if pre != s:
            ans.append(pre)
            ans.append(s)

    if flag:
        continue
    else:
        if len(ans) == 2:
            ans.remove('R')
            flag = True

ans = ''.join(ans)

ans = ans.replace('R', '')

print(ans[::-1] if inv else ans)
