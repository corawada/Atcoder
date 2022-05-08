tmp = input().split(" ")
a = int(tmp[0])
b = int(tmp[1])

if a%2 == 1:
    if b%2 == 1:
        print("Odd")
    else:
        print("Even")
else:
    print("Even")
