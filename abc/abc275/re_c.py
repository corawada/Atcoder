from copy import deepcopy
ans = 0

points = list()
for i in range(9):
    s = input()

    j = -1
    for _ in range(s.count('#')):
        j = s.find('#', j+1)
        points.append([i, j])

re_points = deepcopy(points)
for i, j in points:
    for nj in range(j+1, 10):
        if [i, nj] in re_points:
            step = nj - j
            if ([i+step, j] in re_points) and ([i+step, nj] in re_points):
                ans += 1
        else:
            continue

    for si in range(1, 9):
        for sj in range(1, 9):
            if in_square([i+si, j+sj]) and ([i+si, j+sj] in re_points):
                if in_square([i+sj, j-sj]) and in_square([i+sj+si, j+si-sj]):
                    if ([i+sj, j-si] in re_points) and ([i+sj+si, j-si+sj] in re_points):
                        ans += 1
                else:
                    continue
            else:
                continue
        
    # re_points.remove([i, j])


print(ans)

