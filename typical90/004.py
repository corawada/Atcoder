from collections import defaultdict
h, w = map(int, input().split())
hh = dict()
ww = defaultdict(int)
nn = list()

for i in range(h):
    A = list(map(int, input().split()))
    for idx, a in enumerate(A):
        ww[idx] += a
    hh[i] = sum(A)
    nn.append(A)

for idh, lis in enumerate(nn):
    ans_lis = list()
    for idw, val in enumerate(lis):
        ans_lis.append(str(hh[idh] + ww[idw] - val))
    print(' '.join(ans_lis))




