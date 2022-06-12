from tqdm import tqdm
from random import randint
def func():
    # n, m = map(int, input().split())
    n, m = randint(2, 2000), randint(0, 2000)

    map_n = dict()
    for _ in range(m):
        # a, b = map(int, input().split())
        a, b = randint(1, n), randint(1, n)
        # print(a, b)
        if a in map_n:
            map_n[a].append(b)
        else:
            map_n[a] = [b]

    def dfs(tosi, conp_flag):
        conp_flag[tosi-1] = True
        call_num = 0

        if tosi not in map_n:
            return 0
        for t in map_n[tosi]:
            if conp_flag[t-1]:
                continue
            else:
                call_num += dfs(t, conp_flag) + 1

        return call_num

    ans = 0
    for to in range(1, n+1):
        ans += dfs(to, [False]*n) + 1

    # print(ans)

for _ in tqdm(range(10000)):
    func()


