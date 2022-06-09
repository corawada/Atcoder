from collections import deque


n, k = map(int, input().split())
C = list(map(int, input().split()))[::-1]

color_dic = dict()
color_k = deque()
for _ in range(k):
    c = C.pop()
    color_k.append(c)
    if c not in color_dic.keys():
        color_dic[c] = 1
    else:
        color_dic[c] += 1

now_num = len(color_dic)
max_num = len(color_dic)

for _ in range(n-k):
    c = C.pop()


    de = color_k.popleft()
    color_k.append(c)
    color_dic[de] -= 1
    if color_dic[de] == 0:
        now_num -= 1
        del color_dic[de]
    
    if c not in color_dic.keys():
        color_dic[c] = 1
        now_num += 1
    else:
        color_dic[c] += 1

    max_num = max(max_num, now_num)

print(max_num)







    



