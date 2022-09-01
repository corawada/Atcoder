s = input()

maru = list()
hate = list()
batu = list()


for idx, c in enumerate(s):
    if c == 'o':
        maru.append(idx)
    elif c == 'x':
        batu.append(idx)
    else:
        hate.append(idx)


ans = 0
for i in range(0, 10000):
    pre_ans = "{:04d}".format(i)
    flag = False

    for j in pre_ans:
        if int(j) in batu:
            flag = True
            break
    if flag:
        continue


    for m in maru:
        if str(m) not in pre_ans:
            flag = True
            break
    if flag:
        continue

    ans += 1

print(ans)
