S = input()
T = input()

count = 0
count = 0
sign = -1
for idx, s in enumerate(S):
    if idx == sign:
        continue

    if T[idx] != s:
        if count == 1:
            print("No")
            break
        elif (T[idx+1] == s) and (T[idx] == S[idx+1]):
            sign = idx+1
            count += 1
        else:
            print("No")
            break
else:
    print("Yes")
