from copy import deepcopy

h, w = map(int, input().split())
start = [0, 0]

nn = list()
nn.append(list('#'*(w+2)))
for i in range(h):
    s = '#'
    s += input()
    s += '#'
    if s.find('S') != -1:
        start = [i+1, s.find('S')]

    nn.append(list(s))
nn.append(list('#'*(w+2)))

directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]


flag = False
for si, sj in [[0, -1], [0, 1], [1, 0]]:

    stack = [[start[0]+si, start[1]+sj]]
    if nn[stack[0][0]][stack[0][1]] == '#':
        continue

    nn[start[0]+si][start[1]+sj] = '#'

    stack_ = list()
    for di, dj in directions:
        tar = nn[stack[0][0]+di][stack[0][1]+dj]
        if tar == '.':
            nn[stack[0][0]+di][stack[0][1]+dj] = '#'
            stack_.append([stack[0][0]+di, stack[0][1]+dj])
    stack = deepcopy(stack_)
    stack_ = list()

    while stack or stack_:
        # print()
        # for r in nn:
        #     print(r)

        if len(stack_) == 0:
            for i, j in stack:
                for di, dj in directions:
                    tar = nn[i+di][j+dj]
                    if tar == '.':
                        nn[i+di][j+dj] = '#'
                        stack_.append([i+di, j+dj])
                    elif tar == 'S':
                        flag = True
                        break

                if flag:
                    break
            if flag:
                break
            
            stack = list()
        else:
            for i, j in stack_:
                for di, dj in directions:
                    tar = nn[i+di][j+dj]
                    if tar == '.':
                        nn[i+di][j+dj] = '#'
                        stack.append([i+di, j+dj])
                    elif tar == 'S':
                        flag = True
                        break

                if flag:
                    break
            if flag:
                break
            
            stack_ = list()

    if flag:
        break

if flag:
    print('Yes')
else:
    print('No')

