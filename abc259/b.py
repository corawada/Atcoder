from math import sin, cos, radians, degrees
import math
a, b, d = map(int, input().split())

if (a == 0) and (b == 0):
    print(0, 0)
else:
    tania = a / (math.sqrt(a**2 + b**2))
    tanib = b / (math.sqrt(a**2 + b**2))
    if b == 0:
        if a < 0:
            kakudo = math.pi
        else:
            kakudo = 0
    else:
        kakudo = math.atan2(b, a)

    nagasa = math.sqrt(a**2 + b**2)

    si = sin(kakudo + radians(d))
    co = cos(kakudo + radians(d))

    print(co* nagasa, si*nagasa)
