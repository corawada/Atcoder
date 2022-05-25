from collections import deque
s = input()

if len(s) == 1:
    print("Yes")
elif s == "xx":
    print("Yes")
elif s.find('o') >= 3:
    print("No")
else:
    S = deque(s)
    for _ in range(s.find('o')):
        S.popleft()
    flag = 'o'
    while S:
        if S.popleft() == flag[0]:
            if flag == 'o':
                flag = 'x1'
            elif flag == 'x1':
                flag = 'x2'
            else:
                flag = 'o'
        else:
            print("No")
            break
    else:
        print("Yes")
