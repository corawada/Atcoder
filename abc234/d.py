import heapq

n, k = map(int, input().split())

A = list(map(int, input().split()))

ls_a = A[:k]

heapq.heapify(ls_a)
ans = heapq.heappop(ls_a)
print(ans)

for i in A[k:]:
    if i <= ans:
        print(ans)
    else:
        heapq.heappush(ls_a, i)
        ans = heapq.heappop(ls_a)
        print(ans)

