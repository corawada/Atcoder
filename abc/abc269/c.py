n = int(input())

ans = [0, ]

for i in range(60):
    tmp_ans_ = list()
    if n&(1 << i):
        for tmp in ans:
            tmp_ans_.append(tmp + 2 ** i)

    ans += tmp_ans_

ans = sorted(ans)

for a in ans:
    print(a)

