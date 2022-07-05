import sys
sys.setrecursionlimit(10000)

h, w = map(int, input().split())
q = int(input())

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(y, x):
    # print('call dfs ({} ,{})'.format(y, x))
    # time.sleep(1)
    if (y,x) not in point:
        return False
    elif (y, x) == (y2, x2):
        return True
    elif (y, x) in already_call:
        return False
    else:
        already_call.add((y, x))
        for direc in direction:
            if dfs(y+direc[0], x+direc[1]):
                return True

point = set()
for _ in range(q):
    a, y1, x1, *c = map(int, input().split())
    if a == 1:
        point.add((y1, x1))
    else: 
        y2, x2 = c
        already_call = set()
        if ((y1, x1) in point) and ((y2, x2) in point):
            if dfs(x1, y1):
                print('Yes')
            else:
                print('No')
        else:
            print('No')
