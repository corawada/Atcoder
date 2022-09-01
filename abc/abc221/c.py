I = sorted(list(input()))

a = I.pop()
b = I.pop()

for i in range((len(I)//2)):
    if a >= b:
        b += I.pop()
        a += I.pop()
    else:
        a += I.pop()
        b += I.pop()

print(a, b)

if len(I) % 2 == 0:
    print(int(a) * int(b))
else:
    pre_b = int(b+I[0]) * int(a)
    pre_a = int(a+I[0]) * int(b)
    if pre_b <= pre_a:
        print(pre_a)
    else:
        print(pre_b)
