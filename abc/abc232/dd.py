h, w = map(int, input().split())
nn = list()
nn_ans = [[0]*(w+1) for _ in range(h+1)]

for _ in range(h):
    I = input()
    nn.append(I)

pre_ans = 0
ans = 0
for idx_y, S in enumerate(nn):
    for idx_x, s in enumerate(S):
        if s == '#':
            continue
        if (idx_x == 0) and (idx_y == 0):
            nn_ans[1][1] = 1
        else:
            pre_math = max(nn_ans[idx_y+1][idx_x], nn_ans[idx_y][idx_x+1])
            if pre_math != 0:
                nn_ans[idx_y+1][idx_x+1] = pre_math + 1
    pre_ans = max(nn_ans[idx_y+1])
    ans = max(ans, pre_ans)


print(ans)

