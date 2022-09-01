S = input()
T = input()

ls = len(S)
lt = len(T)

ans = list()
for i in range(ls-lt+1):
    ss = S[i:i+lt]

    for bs, bt in zip(ss, T):
        if (bs == '?') or (bs == bt):
            pass
        else:
            break
    else:
        pre_ans = S[0:i] + T + S[i+lt:]
        ooans = ''
        for a in pre_ans:
            if a == '?':
                ooans += 'a'
            else:
                ooans += a
        ans.append(ooans)

if ans:
    print(min(ans))
else:
    print('UNRESTORABLE')
