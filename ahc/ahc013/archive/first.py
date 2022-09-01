n, k = map(int, input().split())
nn = [input()+'0' for _ in range(n)]
nn.append('0'*(n+1))


joint = list()
for i in range(n):
    for j in range(n):
        point = nn[i][j]
        if point == '0':
            continue

        if point == nn[i+1][j]:
            joint.append([i, j, i+1, j])
        if point == nn[i][j+1]:
            joint.append([i, j, i, j+1])

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



