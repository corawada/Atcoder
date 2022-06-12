n, k = map(int, input().split())

friend_d = dict()
friend_s = set()
for _ in range(n):
    a, b = map(int, input().split())
    if a not in friend_d:
        friend_d[a] = b
        friend_s.add(a)
    else:
        friend_d[a] += b

friend_l = sorted(list(friend_s))[::-1]

now = 0
while k:
    now += k
    k = 0

    if friend_l:
        friend = friend_l.pop()
        if now >= friend:
            k += friend_d[friend]

print(now)







