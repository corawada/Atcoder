T = int(input())

for _ in range(T):
    str_q = input()
    lq = len(str_q)
    tmp_ans = 0
    for i in range(1, lq):
        if lq % i == 0:
            target2 = int(str_q[:i]*(lq//i))
            target = int(str(int(str_q[:i])-1)*(lq//i))
            if target <= int(str_q):
                tmp_ans = max(tmp_ans, target)
            if target2 <= int(str_q):
                tmp_ans = max(tmp_ans, target2)
        else:
            continue

    tmp_ans = max(tmp_ans, int('9'*(lq-1)))
    print(tmp_ans)

