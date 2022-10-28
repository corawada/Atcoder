from math import gcd
from itertools import combinations
n, m = map(int, input().split())

points = list()
po_set = set()
ans_list = list()
line_flag = [[[0]*4 for _ in range(n-1)]for _ in range(n-1)]
# ['right', 'down', 'rightdown', 'rightup']
for _ in range(m):
    x, y = map(int, input().split())
    points.append([x, y])
    po_set.add("{:02}{:02}".format(x, y))

def jadge_in_po(po):
    return True if "{:02}{:02}".format(po[0], po[1]) in po_set else False

def add_po(po):
    points.append([po[0], po[1]])
    po_set.add("{:02}{:02}".format(po[0], po[1]))
    return 0

def add_line(po1, po2):
    if po1[0] == po2[0]: # down
        const_x = po1[0]
        if po1[1] < po2[1]:
            for y in range(po1[1], po2[1]):
                line_flag[const_x][y][1] = 1
        else:
            for y in range(po2[1], po1[1]):
                line_flag[const_x][y][1] = 1
    elif po1[1] == po2[1]: # right
        const_y = po1[1]
        if po1[0] < po2[0]:
            for x in range(po1[0], po2[0]):
                line_flag[x][const_y][0] = 1
        else:
            for x in range(po2[0], po1[0]):
                line_flag[x][const_y][0] = 1
    elif (po2[0]-po1[0]) * (po2[1]-po1[1]) > 0: # rightup
        if po1[0] < po2[0]:
            for x, y in zip(range(po1[0], po2[0]), range(po1[1]+1, po2[1]+1)):
                line_flag[x][y][3] = 1
        else:
            for x, y in zip(range(po2[0], po1[0]), range(po2[1]+1, po1[1]+1)):
                line_flag[x][y][3] = 1
    else: # rightdown
        if po1[0] < po2[0]:
            for x, y in zip(range(po1[0], po2[0]), range(po1[1], po2[1])):
                line_flag[x][y][2] = 1
        else:
            for x, y in zip(range(po2[0], po1[0]), range(po2[1], po1[1])):
                line_flag[x][y][2] = 1
    return 0

def pos_rectangle(new_p, p0, p1, p2):
    if jadge_in_po(new_p):
        return False
    else:
        if not (line_jadge_no(p0, p1) or line_jadge_no(p1, p2) \
                or line_jadge_no(p2, new_p) or line_jadge_no(new_p, p0)):
            return True
        else:
            return False

def line_jadge_no(po1, po2):
    # その線が描画不可能かどうかを調べる
    sx = po2[0]-po1[0]
    sy = po2[1]-po1[1]
    gc = gcd(sx, sy)
    dx = sx // gc
    dy = sy // gc
    for i in range(gc-1):
        # print('jadge [{}, {}]'.format(po1[0]+dx*(i+1), po1[1]+dy*(i+1)))
        if jadge_in_po([po1[0]+dx*(i+1), po1[1]+dy*(i+1)]):
            return True
    else:
        # return False
        if pos_line(po1, po2):
            return True
        else:
            return False

def pos_line(po1, po2):
    if po1[0] == po2[0]: # down
        const_x = po1[0]
        if po1[1] < po2[1]:
            for y in range(po1[1], po2[1]):
                if line_flag[const_x][y][1] == 1:
                    return True
        else:
            for y in range(po2[1], po1[1]):
                if line_flag[const_x][y][1] == 1:
                    return True
    elif po1[1] == po2[1]: # right
        const_y = po1[1]
        if po1[0] < po2[0]:
            for x in range(po1[0], po2[0]):
                if line_flag[x][const_y][0] == 1:
                    return True
        else:
            for x in range(po2[0], po1[0]):
                if line_flag[x][const_y][0] == 1:
                    return True
    elif (po2[0]-po1[0]) * (po2[1]-po1[1]) > 0: # rightup
        if po1[0] < po2[0]:
            for x, y in zip(range(po1[0], po2[0]), range(po1[1], po2[1])):
                if line_flag[x][y][3] == 1:
                    return True
        else:
            for x, y in zip(range(po2[0], po1[0]), range(po2[1], po1[1])):
                if line_flag[x][y][3] == 1:
                    return True
    else: # rightdown
        if po1[0] < po2[0]:
            for x, y in zip(range(po1[0], po2[0]), range(po1[1]-1, po2[1]-1)):
                if line_flag[x][y][2] == 1:
                    return True
        else:
            for x, y in zip(range(po2[0], po1[0]), range(po2[1]-1, po1[1]-1)):
                if line_flag[x][y][3] == 1:
                    return True
    return False

def main():
    def make_new_po(p0, p1, p2):
        ans_po = [-1, ]
        sum_x = p0[0]+p1[0]+p2[0]
        sum_y = p0[1]+p1[1]+p2[1]
        if ((p1[0]-p0[0])*(p2[0]-p0[0]) + (p1[1]-p0[1])*(p2[1]-p0[1]) == 0) and \
                (abs(p1[0]-p0[0]) == abs(p1[1]-p0[1])):
            ans_po = [sum_x-2*p0[0], sum_y-2*p0[1]] # n102
            if pos_rectangle(ans_po, p1, p0, p2):
                add_po(ans_po)
                ans_list.append(list(map(str, \
                        [ans_po[0], ans_po[1], p1[0], p1[1], p0[0], p0[1], p2[0], p2[1]])))
                add_line(ans_po, p0)
                add_line(p0, p1)
                add_line(p1, p2)
                add_line(p2, ans_po)
        elif ((p0[0]-p1[0])*(p2[0]-p1[0]) + (p0[1]-p1[1])*(p2[1]-p1[1]) == 0) and \
                (abs(p1[0]-p0[0]) == abs(p1[1]-p0[1])):
            ans_po = [sum_x-2*p1[0], sum_y-2*p1[1]] # n012
            if pos_rectangle(ans_po, p0, p1, p2):
                add_po(ans_po)
                ans_list.append(list(map(str, \
                        [ans_po[0], ans_po[1], p0[0], p0[1], p1[0], p1[1], p2[0], p2[1]])))
                add_line(ans_po, p0)
                add_line(p0, p1)
                add_line(p1, p2)
                add_line(p2, ans_po)
        elif ((p0[0]-p2[0])*(p1[0]-p2[0]) + (p0[1]-p2[1])*(p1[1]-p2[1]) == 0) and \
                (abs(p2[0]-p0[0]) == abs(p2[1]-p0[1])):
            ans_po = [sum_x-2*p2[0], sum_y-2*p2[1]] # n021
            if pos_rectangle(ans_po, p0, p2, p1):
                add_po(ans_po)
                ans_list.append(list(map(str, \
                        [ans_po[0], ans_po[1], p0[0], p0[1], p2[0], p2[1], p1[0], p1[1]])))
                add_line(ans_po, p0)
                add_line(p0, p1)
                add_line(p1, p2)
                add_line(p2, ans_po)
        else:
            return 0

        if (ans_po[0] < 0) or (n-1 < ans_po[0]):
            return 0
        elif (ans_po[1] < 0) or (n-1 < ans_po[1]):
            return 0

        return ans_po

    # => nake_new_po
    # => pos_rectangle => line_jadge_no
    for p0, p1, p2 in combinations(points, 3):
        tar = make_new_po(p0, p1, p2)

main()
print(len(ans_list))

for ans_raw in ans_list:
    print(" ".join(ans_raw))


# point_sum = 0
# for l1 in line_flag:
#     for l2 in l1:
#         point_sum += sum(l2)
#
# print(point_sum)





