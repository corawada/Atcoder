from collections import deque

N, X = map(int, input().split())
S = deque(input())
new_S = deque('U')

sum_u = 0
while S:
    s = S.popleft()
    if s == 'U':
        if new_S.pop() == 'U':
            sum_u += 1
            new_S.append('U')
    else:
        new_S.append('0' if s=='L' else '1')

new_S.popleft()
new_S.appendleft('0')

X = max(1, X // (2**sum_u))


X = X * (2**(len(new_S)-1)) + int("".join(new_S), 2)

print(X)

    
