n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

mix = list()
for a, b in zip(A, B):
    diff = a-b
    if diff >= 0:
        mix.append([a, b, diff])
    else:
        mix.append([a, b, 10**11])

mix = sorted(mix, key=lambda x:x[2], reverse=True)

sum_diff = sum(A) - sum(B)
if sum_diff < 0:
    print(-1)
else:
    count = 0
    while mix:
        sum_diff -= mix.pop()[2]
        if sum_diff >=0:
            count += 1
        else:
            break
    print(n-count)
