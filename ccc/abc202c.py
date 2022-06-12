n = int(input())
A = sorted(list(map(int, input().split())))
B = list(map(int, input().split()))
C = sorted(list(map(int, input().split())))

c_dict = dict()
for c in C:
    if c not in c_dict:
        c_dict[c] = 1
    else:
        c_dict[c] += 1


b_dict = dict()
for idx, b in enumerate(B):
    if b not in b_dict:
        if idx+1 in c_dict:
            b_dict[b] = c_dict[idx+1]
    else:
        if idx+1 in c_dict:
            b_dict[b] += c_dict[idx+1]

ans = 0
for a in A:
    if a in b_dict:
        ans += b_dict[a]


print(ans)

