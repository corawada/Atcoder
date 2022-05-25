from collections import deque

N = int(input())

L = list()

for _ in range(N):
    L.append(input())

print(len(set(L)))

