from collections import deque

N = int(input())
C = sorted(deque(map(int, input().split())))

for i in range(N-1):
    for _ in range(4):
        flag = C.pop()
    if flag != N-i:
        print(N-i)
        break
else:
    print(1)

    

