n = int(input())
S = input()
W = list(map(int, input().split()))
nn = list()

tmp_ans = S.count('0')
ans = tmp_ans
for s, w in zip(S, W):
    nn.append((w, int(s)))

nn = sorted(nn, key=lambda x: (x[0], x[1]))
print(nn)

for _ in range(n):
    w, s = nn.pop()
    if s == 1:
        tmp_ans += 1
    else:
        tmp_ans -= 1

    ans = max(ans, tmp_ans)

print(ans)

