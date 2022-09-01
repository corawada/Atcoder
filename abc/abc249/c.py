n, k = map(int, input().split())

s = [input() for i in range(n)]

counta = 0
for i in range(2**n):
    msk = "{num:0{width}b}".format(num=i, width=n)
    
    char_s = ""
    for idx, c in enumerate(msk):
        if c == "1":
            char_s += s[idx]
    char_l = list(set(char_s))

    tmp_counta = 0
    for j in char_l:
        if char_s.count(j) == k:
            tmp_counta += 1
    counta = max(counta, tmp_counta)

print(counta)

