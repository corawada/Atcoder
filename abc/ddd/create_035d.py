from random import randint

n = randint(2, 15)
m = randint(1, n*(n-1))
t = randint(5, 100)

print(n, m, t)

a_list = list()
for _ in range(n):
    a_list.append(str(randint(1, 20)))

print(' '.join(a_list))

for _ in range(m):
    while True:
        a, b, c = randint(1, n), randint(1, n), randint(1, 100)
        if a != b:
            break

    print('{} {} {}'.format(a, b, c))

