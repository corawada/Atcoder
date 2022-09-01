n, Q = map(int, input().split())
S = input()

point = 0
for _ in range(Q):
    q, x = map(int, input().split())
    if q == 1:
        point = (point - x) % n
    else:
        print(S[(point + x - 1) % n])
