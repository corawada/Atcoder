from collections import deque
from bisect import bisect
import heapq

n, k = map(int, input().split())
P = deque(map(int, input().split()))

card = [-1] * n
card_q = dict()
card_list = list()
heapq.heapify(card_list)
for i in range(1,n+1):
    p = P.popleft()
    num = bisect(card_list, p)
    if num == len(card_list):
        heapq.heappush(card_list, p)
        card_q[p] = [p,]
    else:
        tmp = card_list[num]
        card_list[num] = p
        card_q[p] = card_q[tmp] 
        card_q[p].append(p)
        del card_q[tmp]

    if len(card_q[p]) == k:
        for c in card_q[p]:
            card[c-1] = i
        del card_q[p]
        card_list.remove(p)

for ans in card:
    print(ans)




