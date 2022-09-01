S = input()

sn = [S]

for _ in range(len(S)-1):
    S = S[-1]+S[0:-1]
    sn.append(S)

max_s = S
min_s = S

for s in sn:
    if max_s < s:
        max_s = s
    if min_s > s:
        min_s = s

print(min_s)
print(max_s)
