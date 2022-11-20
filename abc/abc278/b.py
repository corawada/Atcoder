a, b = map(int, input().split())

def jadge(h, m):
    if (0 <= int(h) <= 23) and (0 <= int(m) <= 59):
        return True
    else:
        return False

while True:
    a_str = "{:02d}".format(a)
    b_str = "{:02d}".format(b)

    if jadge(a_str[0]+b_str[0], a_str[1]+b_str[1]):
        print(a, b)
        break

    b += 1
    if b == 60:
        a += 1
        b = 0
        if a == 24:
            a = 0

    
