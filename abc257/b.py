n, k, q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

nn = dict()

for idx, a in enumerate(A):
    nn[idx+1] = a

for l in L:
    if l+1 not in nn:
        if nn[l] == n:
            continue
        else:
            nn[l] += 1
            continue
    if nn[l] == n:
        continue
    elif nn[l+1] == nn[l] + 1:
        continue
    else:
        nn[l] = nn[l]+1


for i in range(1, k+1):
    print(nn[i], end=' ')








