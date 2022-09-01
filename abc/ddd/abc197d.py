import math
n = int(input())
px, py = map(int, input().split())
px2, py2 = map(int, input().split())

point = [(px+px2)/2 , (py+py2)/2]

p1 = [px-point[0], py-point[1]]

sita = 2 * math.pi / n

pre_x = math.cos(sita) * p1[0] -math.sin(sita) * p1[1] + point[0]
pre_y = math.cos(sita) * p1[1] +math.sin(sita) * p1[0] + point[1]

print(pre_x, pre_y)
