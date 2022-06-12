n = int(input())

def jadge(sec, tar_sec):
    if (sec[1] < tar_sec[1] < sec[2]) \
            or (sec[1] < tar_sec[2] < sec[2]) \
            or (tar_sec[1] < sec[1] < tar_sec[2]):
        return True
    elif sec[1] == tar_sec[1]:
        return True
    elif sec[1] == tar_sec[2]:
        if ((sec[0] == 1) or (sec[0] == 2)) and ((tar_sec[0] == 1) or (tar_sec[0] == 3)):
            return True
    elif sec[2] == tar_sec[1]:
        if ((sec[0] == 1) or (sec[0] == 3)) and ((tar_sec[0] == 1) or (tar_sec[0] == 2)):
            return True
    
    return False

sec_list = [list(map(int, input().split()))]

ans = 0
for _ in range(n-1):
    target = list(map(int, input().split()))
    for s in sec_list:
        if jadge(s, target):
            ans += 1
    sec_list.append(target)

print(ans)

