from pprint import pprint
n = int(input())
nn = list()

for _ in range(n):
    s_lis = input()*3
    nn.append(s_lis)


nn.extend(nn)
nn.extend(nn)

dir_x = [0, 1, -1]
dir_y = [0, 1, -1]


ans = 0
for i in range(n, 2*n):
    for j in range(n, 2*n):
        for sx in dir_x:
            for sy in dir_y:
                if (sx == 0) and (sy == 0):
                    continue
                pre_ans = ''
                for k in range(n):
                    pre_ans += nn[i+sx*k][j+sy*k]

                ans = max(ans, int(pre_ans))

print(ans)




