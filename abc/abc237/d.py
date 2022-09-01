from collections import deque


n = int(input())

S = input()[::-1]

ans = deque([str(n),])

for idx, s in enumerate(S):
    if s == 'R':
        ans.appendleft(str(n-idx-1))
    else:
        ans.append(str(n-idx-1))

print(" ".join(list(ans)))

 
