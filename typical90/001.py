from collections import deque

n, l = map(int, input().split())
k = int(input())
A = list(map(int, input().split()))

def solve(arg):
    sp_time = 0
    value = 0
    for a in A:
        if a - value < arg:
            continue
        else:
            sp_time += 1
            value = a
    if sp_time < k:
        return False
    elif sp_time == k:
        if l - value < arg:
            return False
        else:
            return True
    else:
        return True

bs_l = 1
bs_r = l//(k+1) + 1
while (bs_r - bs_l) > 1:
    bs_i = (bs_l + bs_r)//2
    if solve(bs_i):
        bs_l = bs_i
    else:
        bs_r = bs_i

print(bs_l)






