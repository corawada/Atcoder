# 基本方針
# 移動はしないで、直線同士で結べるノードのみ結ぶ
# 線が交差しないように、線を引いた箇所には'e'を代入する

n, k = map(int, input().split())
nn = [list(input()+'e') for _ in range(n)]
nn.append('e'*(n+1))


joint = list()
for i in range(n):
    for j in range(n):
        point = nn[i][j]
        if (point == '0') or (point == 'e'):
            continue

        # 下に探す
        for si in range(1, n):
            if nn[i+si][j] == '0':
                continue
            else:
                if nn[i+si][j] == point:
                    joint.append([i, j, i+si, j])

                    for hi in range(i+1, i+si):
                        nn[hi][j] = 'e'
                
                break

        # 右に探す
        for sj in range(1, n):
            if nn[i][j+sj] == '0':
                continue
            else:
                if nn[i][j+sj] == point:
                    joint.append([i, j, i, j+sj])

                    for hj in range(j+1, j+sj):
                        nn[i][hj] = 'e'
                
                break

# print(joint)
# print(len(joint))


# ===== SUBMIT =====
print(0)




if len(joint) <= k * 100:
    print(len(joint))
    for an in joint:
        print(' '.join([str(i) for i in an]))
else:
    print(k*100)
    for an in joint[:k*100]:
        print(' '.join([str(i) for i in an]))



