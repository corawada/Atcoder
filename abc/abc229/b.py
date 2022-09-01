a, b = map(int, input().split())

a = "{:019d}".format(a)
b = "{:019d}".format(b)

for i in range(19):
    if len(str(int(a[i]) + int(b[i]))) != 1:
        print("Hard")
        break
else:
    print("Easy")
