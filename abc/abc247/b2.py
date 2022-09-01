n = int(input())

s = list()
t = list()

for k in range(n):
    pre_s, pre_t = map(str, input().split())
    s.append(pre_s)
    t.append(pre_t)


for i in range(2**n):
    a = list()
    mask = "{msk:0{num}b}".format(msk=i, num=n)
    for j in range(n):
        if mask[j] == 0:
            a.append(s[j])
        else:
            a.append(t[j])
    else:
        if len(set(a)) != n:
            print("No")
            break
else:
    print("Yes")

    
