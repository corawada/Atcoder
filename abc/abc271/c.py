n = int(input())
A = list(map(int, input().split()))

a_set = set()
yobun = 0
for a in A:
    if a in a_set:
        yobun += 1
    else:
        a_set.add(a)

A = sorted(a_set)
# print(A, yobun)

counter = 0
while True:
    counter += 1
    # print('now', counter)

    if counter in a_set:
        # print(A, yobun)
        continue
    else:
        if yobun:
            yobun -= 1
        elif A and (counter < A[-1]):
            a_set.remove(A[-1])
            A.pop()

        else:
            break

        # print('kook')
        if yobun:
            yobun -= 1
        elif A and (counter < A[-1]):
            a_set.remove(A[-1])
            A.pop()
        else:
            break

    # print(A, yobun)

print(counter-1)




