n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# from random import randint
# 
# n = randint(1, 15)
# k = 6
# a = [randint(1, 15) for _ in range(n)]
# b = [randint(1, 15) for _ in range(n)]

# print(a)
# print(b)

x_flag = []

x_flag.append(3)
    

for i in range(1, n):
    a_flag = False
    b_flag = False
    if x_flag[-1] == 2: # a はいける
        if abs(a[i-1] - a[i]) <= k:
            a_flag = True
        if abs(a[i-1] - b[i]) <= k:
            b_flag = True
    elif x_flag[-1] == 1: # b はいける
        if abs(b[i-1] - a[i]) <= k: # b => a
            a_flag = True
        if abs(b[i-1] - b[i]) <= k: # b=> b
            b_flag = True
    elif x_flag[-1] == 3:
        if abs(a[i-1] - a[i]) <= k:
            a_flag = True
        elif abs(b[i-1] - a[i]) <= k: # b => a
            a_flag = True
        if abs(a[i-1] - b[i]) <= k:
            b_flag = True
        elif abs(b[i-1] - b[i]) <= k: # b=> b
            b_flag = True

    if a_flag == True:
        if b_flag == True:
            x_flag.append(3)
        else:
            x_flag.append(2)
    else:
        if b_flag == True:
            x_flag.append(1)
        else:
            print("No")
            break
else:
    print("Yes")

# print(x_flag)

