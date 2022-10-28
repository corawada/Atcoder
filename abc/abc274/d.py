n, x, y = map(int, input().split())
A = list(map(int, input().split()))

x_angle = list()
y_angle = list()

flag = 1
for a in A:
    if flag:
        x_angle.append(a)
    else:
        y_angle.append(a)

    flag = abs(flag-1)

x_angle.pop(0)
x_pos = {A[0]}

for p in x_angle:
    x_pos_ = set()
    for pos in x_pos:
        x_pos_.add(pos+p)
        x_pos_.add(pos-p)
    x_pos = x_pos_

y_pos = {y_angle[-1],  -y_angle[-1]}
y_angle.pop()
for p in y_angle:
    y_pos_ = set()
    for pos in y_pos:
        y_pos_.add(pos+p)
        y_pos_.add(pos-p)

    y_pos = y_pos_


if (x in x_pos) and (y in y_pos):
    print("Yes")
else:
    print("No")
