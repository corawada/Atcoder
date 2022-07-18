from collections import deque
n, k = map(int, input().split())
R_point, S_point, P_point = map(int, input().split())
S = input()

s1, s2 = S[:k], S[k:]

result = {'r':0, 's':0, 'p':0}
s_deque = deque()

for s in s1:
    if s == 'r': hand = 'p'
    elif s == 's': hand = 'r'
    else: hand = 's'
    result[hand] += 1
    s_deque.append(hand)

for s in s2:
    if s == 'r': hand = 'p'
    elif s == 's': hand = 'r'
    else: hand = 's'

    result[hand] += 1
    if hand == s_deque.popleft():
        result[hand] -= 1
        hand = 'e'

    s_deque.append(hand)

ans = result['r']*R_point + result['s']*S_point + result['p']*P_point

print(ans)

