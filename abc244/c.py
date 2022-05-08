n = int(input())

empty = [i for i in range(1, 2*(n+1))]

while True:
    print(empty.pop())
    aoki = int(input())
    if aoki != 0:
        empty.remove(aoki)
    else:
        break


    


