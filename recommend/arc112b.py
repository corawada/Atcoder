B, C = map(int, input().split())

c = B - C//2
a = (-1 * B) - (C-1)//2
b = (B - C//2)

if B > 0:
    c = B - C//2
    d = -a - C%2
    a = -B - (C-1)//2
    b = -B + (C-1)//2 

    ans = d-a + min(0,b-c+1) + 1 

elif B == 0:
    a = B - C//2
    d = (-1 * a) - (C+1)%2
    ans = d - a + 1
else:
    a = B - C//2
    d = -a - (C+1)%2 
    c = -B - C//2 + (C+1)%2
    b = B + (C-2)//2

    ans = d-a + min(0,b-c+1) + 1 

if C == 1:
    if B == 0:
        ans = 1
    else:
        ans = 2

print(ans)


# timestamp
# Data     Time     Diff     msg
# 22/07/14 16:22:51 00:00:00 start
# 22/07/14 16:46:20 00:23:29 submit
