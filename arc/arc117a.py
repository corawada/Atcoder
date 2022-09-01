a, b = map(int, input().split())

A = list(range(1, max(a, b)+1))
B = [-i for i in list(range(1, max(a, b)+1))]

if a > b:
    for _ in range(a-b):
        b1, b2 = B.pop(), B.pop()
        B.append(b1 + b2)
elif a < b:
    for _ in range(b-a):
        a1, a2 = A.pop(), A.pop()
        A.append(a1 + a2)
else:
    pass

print(' '.join([str(s) for s in A]), end = ' ')
print(' '.join([str(s) for s in B]), end = ' ')
print()
