n, l, r = map(int, input().split())
A = list(map(int, input().split()))

sum_a = 0
rui_l = [0, ]
ehe_l = [0, ]
for idx, a in enumerate(A):
    sum_a += a
    rui = rui_l[-1] + a
    rui_l.append(rui)
    ehe_l.append(l*(idx+1) - rui)


rui_r = [0, ]
mainasu = [0, ]
min_value = 0
for idx, a in enumerate(A[::-1]):
    rui = rui_r[-1] + a
    rui_r.append(rui)
    koko =  r*(idx+1) - rui
    if min_value >= koko:
        min_value = koko
    mainasu.append(min_value)

mainasu = mainasu[::-1]

diff = 0
for ll, rr in zip(ehe_l, mainasu):
    diff = min(diff, ll+rr)

print(sum_a + diff)

