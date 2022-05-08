num = int(input())
li = list(map(int, input().split()))

count = 0
while count != -1:
    for idx, value in enumerate(li):
        if value%2 == 1:
            print(count)
            count = -2
            break
        else:
            li[idx] = value/2
    count += 1

