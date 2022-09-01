n = int(input())

s = list()
t = list()
all_name = list()

for i in range(n):
    pre_s, pre_t = map(str, input().split())

    s.append(pre_s)
    t.append(pre_t)
    
    all_name.append(pre_s)
    all_name.append(pre_t)

for i in range(n):
    if all_name.count(s[i]) == 1:
        continue
    elif all_name.count(s[i]) == 2:
        if s[i] == t[i]:
            continue
        elif all_name.count(t[i]) == 1:
            continue
        else:
            print("No")
            break
    else:
        if all_name.count(t[i]) == 1:
            continue
        else:
            print("No")
            break
else:
    print("Yes")

