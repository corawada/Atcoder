s = list(input().split())
takahashi = list(input().split())

ids = [0, 0, 0]

for idx, val in enumerate(takahashi):
    if val == "R":
        ids[0] = s[idx]
    elif val == "G":
        ids[1] = s[idx]
    else:
        ids[2] = s[idx]

flag = 0
for idx, iro in enumerate(["R", "G", "B"]):
    if ids[idx] == iro:
        flag += 1

if flag == 1:
    print("No")
else:
    print("Yes")



    
