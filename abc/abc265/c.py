h, w = map(int, input().split())

table = list()
for _ in range(h):
    table.append(input())

def point_to(i, j):
    return i*w + j%w

def point_from(x):
    return [x//w, x%w]

now = 0

already = set()
while True:
    poi = point_from(now)
    dire = table[poi[0]][poi[1]]
    next_poi = poi.copy()
    if dire == 'U':
        next_poi[0] -= 1
    elif dire == 'D':
        next_poi[0] += 1
    elif dire == 'L':
        next_poi[1] -= 1
    elif dire == 'R':
        next_poi[1] += 1
    
    print(next_poi)
    now = point_to(next_poi[0], next_poi[1])
    if now in already:
        print(-1)
        break

    if (0 <= next_poi[0] <= h-1) and (0 <= next_poi[1] <= w-1):
        already.add(point_to(poi[0], poi[1]))
    else:
        print(' '.join([str(s+1) for s in poi]))
        break

print(len(already))
    

