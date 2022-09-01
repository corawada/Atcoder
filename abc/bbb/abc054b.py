n, m = map(int, input().split())

nn = list()
mm = list()
for _ in range(n):
    nn.append(input())

for _ in range(m):
    mm.append(input())


ans = False
for i in range(n-m+1):
    for j in range(n-m+1):
        for idxi, si in enumerate(mm):
            flag = True
            for idxj, sj in enumerate(si):
                if nn[i+idxi][j+idxj] == sj:
                    continue
                else:
                    flag = False
                    break
            if flag == False:
                break
        else:
            ans = True

print('Yes' if ans else 'No')





# timestamp
# Data     Time     Diff     msg
# 22/07/27 21:53:39 00:00:00 start
# 22/07/27 22:19:47 00:26:08 first
