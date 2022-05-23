n, k = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

max_a = 0
max_a_idx = list()

for i, a in enumerate(A):
    if a >= max_a:
        max_a = a

for i in range(len(A)):
    if A[i] == max_a:
        max_a_idx.append(i+1)

for b in B:
    if b in max_a_idx:
        print("Yes")
        break
else:
    print("No")


