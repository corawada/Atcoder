from itertools import permutations, combinations
n, m = map(int, input().split())

strings = list()
for _ in range(n):
    strings.append(input())

already = set()
for _ in range(m):
    already.add(input())

flag = False
under_space = n - 1
for s_tuple in permutations(strings, n):
    strings_length = sum([len(s) for s in s_tuple])
    if strings_length + under_space > 16:
        continue
    elif strings_length + under_space < 3:
        continue

    for indexs in combinations(range(17-strings_length), n):
        s_under = list()
        for i in range(n-1):
            s_under.append(indexs[i+1] - indexs[i])

        tmp_ans = ''
        for i in range(under_space):
            tmp_ans += s_tuple[i]
            tmp_ans += '_' * s_under[i]
        tmp_ans += s_tuple[-1]

        # print(tmp_ans)
        if tmp_ans not in already:
            print(tmp_ans)
            flag = True
            break

    if flag:
        break
else:
    print(-1)

