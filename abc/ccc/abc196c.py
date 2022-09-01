n = input()

l = len(n) // 2

if len(n) == 1:
    print(0)
elif len(n) % 2 == 1:
    print('9'*l)
elif l == 1:
    if n[0] > n[1]:
        print(int(n[0])-1)
    else:
        print(n[0])
else:
    ans = int('9'*((l) - 1))
    if n[:l] > n[l:]:
        ans += int(n[:l]) - 10**(l - 1)
    else:
        ans += int(n[:l]) - 10**(l - 1) +1

    print(ans)

