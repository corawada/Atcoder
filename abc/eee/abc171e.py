n = int(input())
A = list(map(int, input().split()))


full = A[0]
for a in A[1:]:
    full ^= a

# print(full)

for a in A:
    print(full ^ a, end=' ')

print()

