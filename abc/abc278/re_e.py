H, W, n, h, w = map(int, input().split())

nn = list()
for _ in range(H):
    nn.append(list(map(int, input().split())))

imos_nn = [[[0]*n for _ in range(W+1)] for _ in range(H+1)]

for i in range(H-1, -1, -1):
    imos = [0]*n
    for j in range(W-1, -1, -1):
        imos[nn[i][j]-1] += 1
        imos_nn[i][j] = imos.copy()

for j in range(W-1, -1, -1):
    imos = imos_nn[H-1][j]
    for i in range(H-2, -1, -1):
        imos = [x+y for x, y in zip(imos, imos_nn[i][j])]
        imos_nn[i][j] = imos.copy()

ans_nn = list()
for k in range(0, H-h+1):
    row_ans = list()
    for l in range(0, W-w+1):
        tmp_ans = [a-b-c+d for a, b, c, d in zip(\
                imos_nn[k][l], \
                imos_nn[k][l+w], \
                imos_nn[k+h][l], \
                imos_nn[k+h][l+w])]

        row_ans.append(sum([(s-p)!=0 for s, p in zip(imos, tmp_ans)]))
    ans_nn.append(row_ans)

for row in ans_nn:
    print(' '.join([str(ans) for ans in row]))
