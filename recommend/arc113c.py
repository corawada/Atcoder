from collections import deque
S = list(input())

renzoku = deque([['abc', 0],])
pre_s = 'abc'
for idx, s in enumerate(S[::-1]):
    if s == pre_s:
        if renzoku[-1][0] == s:
            if renzoku[-1][-1] != idx-2:
                renzoku.pop()
                renzoku.append([s, idx-1])
        else:
            renzoku.append([s, idx-1])

    pre_s = s

renzoku.popleft()

ans = 0
pre_num = 0
while renzoku:
    str_s, num = renzoku.popleft()
    ans += num
    time = num-pre_num
    pre_num = num
    for _ in range(time):
        if S.pop() == str_s:
            ans -= 1

print(ans)



# timestamp
# Data     Time     Diff     msg
# 22/07/24 13:08:34 00:00:00 start
# 22/07/24 13:50:45 00:42:11 first_submit
