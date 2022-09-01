n = int(input())
A = list(map(int, input().split()))

count = 1
now = n
while True:
    now = A[now-2]
    if now == 1:
        break
    else:
        count += 1

print(count)


