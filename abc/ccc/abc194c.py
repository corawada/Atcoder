from random import randint
"""
n = int(input())
A = list(map(int, input().split()))
"""

n = 3 * 10 ** 3
A = [randint(-200, 200) for _ in range(n)]

a_dic = dict()
for a in A:
    if a in a_dic:
        a_dic[a] += 1
    else:
        a_dic[a] = 1


ans = 0
for a in A:
    a_dic[a] -= 1
    for key, value in a_dic.items():
        ans += (a-key)**2 * value


print(ans)

