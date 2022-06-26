n = int(input())
S = input()
W = list(map(int, input().split()))

nn = list()
nn_dict = dict()

tmp_ans = S.count('0')
ans = tmp_ans
for s, w in zip(S, W):
    nn.append(w)
    if w in nn_dict:
        if s == '0':
            nn_dict[w][0] += 1
        else:
            nn_dict[w][1] += 1
    else:
        if s == '0':
            nn_dict[w] = [1, 0]
        else:
            nn_dict[w] = [0, 1]

nn = sorted(list(set(nn)))

for _ in range(len(nn)):
    w = nn.pop()
    tmp_ans += nn_dict[w][1] - nn_dict[w][0]
    ans = max(ans, tmp_ans)

print(ans)



