num = int(input())

tmp_t = 0
tmp_x = 0
tmp_y = 0

for i in range(num):
    tar_t, tar_x, tar_y = map(int, input().split())
    
    d  = (tar_t-tmp_t) - (abs(tar_x - tmp_x) + abs(tar_y - tmp_y))   
    if  not ((d>=0) and (d%2==0)):
        print("No")
        break

    tmp_t = tar_t
    tmp_x = tar_x
    tmp_y = tar_y
else:
    print("Yes")

