n = int(input())
A = list(map(int, input().split()))

num_dic = dict()
re_num = dict()
for idx, a in enumerate(A):
    num_dic[idx+1] = a
    re_num[a] = idx + 1

already = set()
target = 1
ans_lis = list()
while (target != n):
    if len(ans_lis) >= n:
        ans_lis = []
        break
    elif re_num[target] == target:
        target += 1
    else:
        for i in range(re_num[target], target, -1):
            if i in already:
                ans_lis = []
                break
            ans_lis.append(i)
            already.add(i)
            re_num[num_dic[i]] += 1
            num_dic[i] = num_dic[i-1]
        target += 1

if len(ans_lis) == n-1:
    for ans in ans_lis:
        print(ans-1)
else:
    print(-1)



