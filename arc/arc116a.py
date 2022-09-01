t = int(input())

for _ in range(t):
    n = int(input())
    if n % 2 == 0:
        if n % 4 == 0:
            print('Even')
        else:
            print('Same')

    else:
        print('Odd')

