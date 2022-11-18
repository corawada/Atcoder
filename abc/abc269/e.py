n = int(input())

l = 1
r = n
while r - l != 0:
    target = (r + l)//2
    print('? 1 {} 1 {}'.format(target, n))
    ans = int(input())

    if ans == -1:
        break
    elif ans == target:
        l = target + 1
    else:
        r = target

lost_h = l

l = 1
r = n
while r - l != 0:
    target = (r + l)//2
    print('? 1 {} 1 {}'.format(n, target))
    ans = int(input())

    if ans == -1:
        break
    elif ans == target:
        l = target + 1
    else:
        r = target

print('! {} {}'.format(lost_h, r))

    

