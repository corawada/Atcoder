n = int(input())

A = input()

count = 0
for num in range(1000):
    str_n = '{:03d}'.format(num)

    first = A.find(str_n[0])

    if first != -1:
        second = A.find(str_n[1], first+1)

        if second != -1:
            third = A.find(str_n[2], second+1)

            if third != -1:
                count += 1

print(count)

