import heapq
n = int(input())

bag = list()
heapq.heapify(bag)

offset = 0

for _ in range(n):
    que = list(map(int, input().split()))
    if que[0] == 1:
        heapq.heappush(bag, que[1]-offset)
    elif que[0] == 2:
        offset += que[1]
    else:
        pre_ans = heapq.heappop(bag)
        print(pre_ans + offset)



