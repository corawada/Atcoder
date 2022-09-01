# 対象のセルの上下左右を調べる
def round_search(array, n, i, j, boder=100):
    """
    necessary : n
    return [bool, [up, down, left, right], [step, step, step, step]]
    """
    # 上を探す
    temp = [9, 9, 9, 9]
    temp_len = [100, 100, 100, 100]
    for step in range(1, min(boder, i+1)):
        tar = int(array[i-step][j])
        if tar == 0: continue
        elif tar == 9:
            temp[0] = 9
            break
        else:
            temp[0] = tar
            temp_len[0] = step
            break

    # 下を探す
    for step in range(1, min(boder, n-i)):
        tar = int(array[i+step][j])
        if tar == 0: continue
        elif tar == 9:
            temp[1] = 9
            break
        else:
            temp[1] = tar
            temp_len[1] = step
            break

    # 左を探す
    for step in range(1, min(boder, j+1)):
        tar = int(array[i][j-step])
        if tar == 0: continue
        elif tar == 9:
            temp[2] = 9
            break
        else:
            temp[2] = tar
            temp_len[2] = step
            break

    # 右を探す
    for step in range(1, min(boder, n-j)):
        tar = int(array[i][j+step])
        if tar == 0: continue
        elif tar == 9:
            temp[3] = 9
            break
        else:
            temp[3] = tar
            temp_len[3] = step
            break

    if int(array[i][j])  == 0:
        print([0, temp, temp_len], i, j)
        return [0, temp, temp_len]
    else:
        print([1, temp, temp_len], i, j)
        return [1, temp, temp_len]

# k == 2 の時に用いる
# 1あるいは2がいてはいけない箇所を作り、移動する
def restricted_for_2(array, n, k):
    tmp_trans = []
    if k == 2:
        for i in range(n):
            for j in range(n):
                if (array[i][j] == '1') and (i%2==0) and (j%2==0):
                    same_count = 0
                    for si, sj in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
                        if array[i+si][j+sj] == '0':
                            _, num, step = round_search(array, n, i+si, j+sj)
                            if same_count < num.count(1) - 1:
                                same_count = num.count(1) - 1
                                xx = [si, sj]
                    else:
                        if same_count != 0:
                            array[i+xx[0]][j+xx[1]] = array[i][j]
                            array[i][j] = '0'
                            tmp_trans.append([i, j, i+si, j+sj])


                elif (array[i][j] == '2') and (i%2==1) and (j%2==1):
                    same_count = 0
                    for si, sj in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
                        if array[i+si][j+sj] == '0':
                            _, num, step = round_search(array, n, i+si, j+sj)
                            if same_count < num.count(2) - 1:
                                same_count = num.count(2) - 1
                                xx = [si, sj]
                    else:
                        if same_count != 0:
                            array[i+xx[0]][j+xx[1]] = array[i][j]
                            array[i][j] = '0'
                            tmp_trans.append([i, j, i+si, j+sj])

    return tmp_trans



