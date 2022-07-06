S = input()
n = len(S)

count_lr = list()

# Rの場合の、右にある連続したLをかずえる
count_R = list()
counter = 0
for s in S[::-1]:
    if s == 'R':
        count_R.append(counter)
        counter = 0
    else:
        counter += 1
        count_R.append(counter)

count_R = count_R[::-1]



count_L = list()
counter = 0
for s in S:
    if s == 'L':
        count_L.append(counter)
        counter = 0
    else:
        counter += 1
        count_L.append(counter)

# print(count_R)
# print(count_L)
# print(n)

ans = list()
for s, cr, cl in zip(S, count_R, count_L):
    if s == 'R':
        if cr != 0:
            ans.append(((cl+1)//2)+(cr//2))
        else:
            ans.append(0)
    else:
        if cl != 0:
            ans.append((cl//2)+((cr+1)//2))
        else:
            ans.append(0)

# print(ans)
print(" ".join([str(i) for i in ans]))


