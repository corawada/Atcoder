s1 = input()
s2 = input()

if s1[0] == '.':
    if s2[1] == '.':
        print("No")
    else:
        print("Yes")
elif s1[1] == '.':
    if s2[0] == '.':
        print("No")
    else:
        print("Yes")
else:
    print("Yes")

