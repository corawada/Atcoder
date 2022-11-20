from collections import defaultdict
H, W, n, h, w = map(int, input().split())

nn = dict()

number_dict = defaultdict(int)

for i in range(H):
    s = list(map(int, input().split()))
    # nn.append(s)

    dict_s = {j:s[j] for j in range(W)}

    nn[i] = dict_s
    for c in s:
        number_dict[c] += 1

ans_list = list()
for k in range(0, H-h+1):
    ans_list_ = list()
    l = 0

    numbers = defaultdict(int)

    for i in range(k, k+h):
        for j in range(l, l+w):
            numbers[nn[i][j]] += 1

    tmp_ans = 0
    for key, value in number_dict.items():
        if key not in numbers:
            tmp_ans += 1
        else:
            if value - numbers[key] > 0:
                tmp_ans += 1

    ans_list_.append(tmp_ans)

    for step in range(1, W-w+1):
        for i in range(k, k+h):
            numbers[nn[i][step-1]] -= 1
            numbers[nn[i][step+w-1]] += 1

        tmp_ans = 0
        for key, value in number_dict.items():
            if key not in numbers:
                tmp_ans += 1
            else:
                if value - numbers[key] > 0:
                    tmp_ans += 1

        ans_list_.append(tmp_ans)

    ans_list.append(ans_list_)

for ans in ans_list:
    print(" ".join([str(a) for a in ans]))
