n = int(input())

if n % 2 == 1:
    pass
else:
    n = n//2
    ss = dict()
    ss[1] = {'()'}
    i = 1

    for i in range(2,n+1):
        # i = 2, 3, 4, 5, ..., n
        ss[i] = set()
        for s in ss[i-1]:
            ss[i].add('('+s+')')
        for k in range(1, i):
            for x in ss[k]:
                for y in ss[i-k]:
                    ss[i].add(x+y)

    ans_l = sorted(list(ss[i]))
    for ans in ans_l:
        print(ans)



    
