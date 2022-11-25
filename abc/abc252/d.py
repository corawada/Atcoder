n = int(input())

A = sorted(list(map(int, input().split())))

print(A)

multiple = 1

now = A[0]
count = 1

for a in A[1:]:
    if a == now:
        count += 1
    else:
        multiple *= count
        count = 1
        now = a
multiple *= count

print(multiple)

lena = len(set(A))

print((lena*(lena-1)*(lena-2)*multiple)//6)

    


