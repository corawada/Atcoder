n, k = map(int, input().split())
A = list(map(int, input().split()))

left = A[k-1]
right = A[k]

book = dict()
re_book = dict()

right_target = -10**10
left_target = 10**10
flag = False
for idx, a in enumerate(A):
    if idx < k:
        if a < right:
            flag = True
            right_target = max(right_target, idx)
    else:
        if a > left:
            flag = True
            left_target = min(left_target, idx)
            break

if flag:
    print(min(k-right_target, left_target-k+1))
else:
    print(-1)

