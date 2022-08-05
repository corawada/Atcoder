h, w, k = map(int, input().split())
S = list()

for _ in range(h):
    S.append(input())


ans = 0
for hbit in range(2**h):
    hb = '{num:0{numl}b}'.format(num=hbit, numl=h)

    for wbit in range(2**w):
        wb = '{num:0{numl}b}'.format(num=wbit, numl=w)

        count = 0
        for i, si in enumerate(S):
            for j, c in enumerate(si):
                if (c=='#') and (hb[i]=='0') and (wb[j]=='0'):
                    count += 1
        if count == k:
            ans += 1

print(ans)
