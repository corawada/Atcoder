import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

n = int(input())
A = list(map(int, input().split()))
A = [i%200 for i in A]

a_dic = dict()

for a in A:
    if a in a_dic:
        a_dic[a] += 1
    else:
        a_dic[a] = 1

ans = 0
for di in a_dic.values():
    if di >= 2:
        ans += combinations_count(di, 2)

print(ans)



