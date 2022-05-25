N, M = map(int, input().split())

B = list(map(int, input().split()))

flag = True
for i, b in enumerate(B):
    if b % 7 == 0:
        if i != M-1:
            flag = False

pre_b = B[0] + 1
for j in B[1:]:
    if pre_b != j:
        flag = False
    pre_b += 1

next_b = " ".join([str(i+7) for i in B])
for j in range(N-1):
    B = list(map(int, next_b.split()))
    b = input()
    if next_b != b:
        flag = False
    next_b = " ".join(str(i+7) for i in B)

print("Yes" if flag else "No")




