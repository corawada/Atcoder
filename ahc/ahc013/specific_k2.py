n, k = map(int, input().split())
raw_nn = list()
for _ in range(n):
    raw_nn.append(list(input() + '9'))
raw_nn.append(list('9'*(n+1)))

flag = False
if k == 2:
    trans = list()
    for i in range(n):
        for j in range(n):
            flag = False
            if (raw_nn[i][j] == '1') and (i%2==0) and (j%2==0):
                for si in range(0, 2):
                    for sj in range(-1, 2):
                        if raw_nn[i+si][j+sj] == '0':
                            raw_nn[i+si][j+sj] = raw_nn[i][j]
                            raw_nn[i][j] = '0'
                            trans.append([i, j, i+si, j+sj])
                            flag = True
                            break
                    if flag:
                        break
            elif (raw_nn[i][j] == '2') and (i%2==1) and (j%2==1):
                for si in range(0, 2):
                    for sj in range(-1, 2):
                        if raw_nn[i+si][j+sj] == '0':
                            raw_nn[i+si][j+sj] = raw_nn[i][j]
                            raw_nn[i][j] = '0'
                            trans.append([i, j, i+si, j+sj])
                            flag = True
                            break
                    if flag:
                        break

    joint = list()
    for iki in range(1, n+1):
        for i in range(n):
            for j in range(n):
                point = raw_nn[i][j]
                if (point == '0') or (point == '9'):
                    continue

                # 下に探す
                for si in range(1, iki+1):
                    if raw_nn[i+si][j] == '0':
                        continue
                    else:
                        if (si == iki) and (raw_nn[i+si][j] == point):
                            joint.append([i, j, i+si, j])

                            for hi in range(i+1, i+si):
                                raw_nn[hi][j] = '9'
                        
                        break

                # 右に探す
                for sj in range(1, iki+1):
                    if raw_nn[i][j+sj] == '0':
                        continue
                    else:
                        if (sj == iki) and (raw_nn[i][j+sj] == point):
                            joint.append([i, j, i, j+sj])

                            for hj in range(j+1, j+sj):
                                raw_nn[i][hj] = '9'
                        
                        break

    print(len(trans))
    for a, b, c, d in trans:
        print(a, b, c, d)
    joint_print_len = min(len(joint),k*100-len(trans))
    print(joint_print_len)
    for idx in range(joint_print_len):
        a, b, c, d = joint[idx]
        print(a, b, c, d)

else:
    print(0)
    print(0)
