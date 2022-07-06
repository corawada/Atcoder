from collections import deque
n, k = map(int, input().split())
S = input()

s_earler_nums = deque([[n-1, 10**6],])
earler_num = [S[-1], n-1]

for idx, s in enumerate(S[-2::-1]):
    print(s)
    # 本当のidx
    real_idx = n - idx - 2

    s_earler_nums.append([real_idx, earler_num[1], s])

    if s <= earler_num[0]:
        earler_num = [s, real_idx]
        
print(s_earler_nums)
print(earler_num)

ans = earler_num[0]
for i in range(k-1):
    print(ans)
    front = s_earler_nums[n-earler_num[1]-3]
    print(front)
    earler_num = [front[2], front[0]]
    ans += earler_num[0]

print(ans)
    














