from collections import deque

def cong(list_t, list_a):
    # print("call func(cong)")
    count_t = [len(taka[i-1]) for i in list_t]
    count_a = [len(aoki[i-1]) for i in list_a]
    # print(count_t)
    # print(count_a)
    if sorted(count_t) == sorted(count_a):
        return True
    else:
        return False

def dfs(d, rem_t, rem_a):
    # print("----------")
    print("call func depth: {}".format(d))
    # print("rem_t: {}".format(rem_t))
    # print("rem_a: {}".format(rem_a))
    if d == N:
        return True

    target = len(rem_t[0])
    flag = True
    for ao in rem_a:
        if len(ao) == target:
            if cong(list(rem_t[0]), ao):
                rem_a.remove(ao)
                rem_t.popleft()
                if dfs(d+1, rem_t.copy(), rem_a.copy()):
                    return True
    return False

N, M = map(int, input().split())

taka = [[] for _ in range(N)]
taka_num = [0 for _ in range(N)]
aoki = [[] for _ in range(N)]
aoki_num = [0 for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    taka[a-1].append(b)
    taka[b-1].append(a)
    taka_num[a-1] += 1
    taka_num[b-1] += 1

for _ in range(M):
    a, b = map(int, input().split())
    aoki[a-1].append(b)
    aoki[b-1].append(a)
    aoki_num[a-1] += 1
    aoki_num[b-1] += 1


print("sort taka_num : {}".format(taka_num))
print("sort aoki_num : {}".format(aoki_num))
print(taka)
print(aoki)


# 条件２：次数列が等しいかを判断
if sorted(taka_num) == sorted(aoki_num):
    if dfs(0, deque(taka).copy(), aoki.copy()):
        print("Yes")
    else:
        print("No")
else:
    print("No")
    # print("joukenn2")

