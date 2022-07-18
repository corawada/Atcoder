from math import floor, ceil
t, n = map(int, input().split())

bai = (100+t)/100
"""
print(bai)
print(t/100)

print('*'*20)


for j in range(1,4):
    print(ceil(100*j/t)+(j-1))


for i in range(1, 30):
    print(i, bai*i)
"""

print(ceil(100*n/t)+(n-1))



# timestamp
# Data     Time     Diff     msg
# 22/07/11 19:31:01 00:00:00 start
# 22/07/11 20:09:11 00:38:10 submit
