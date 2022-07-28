n = int(input())

nn = list()

for _ in range(n):
    nn.append(tuple(input()))

pre_t_nn = list(zip(*nn))

t_nn = list()
for t_n in pre_t_nn:
    emp_list = list()
    for t in t_n:
        if t == 'W':
            t = 'L'
        elif t == 'L':
            t = 'W'
        emp_list.append(t)
    t_nn.append(tuple(emp_list))


if nn==t_nn:
    print('correct')
else:
    print('incorrect')
