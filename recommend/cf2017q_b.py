n, m, k = map(int, input().split())

flag = False
for a in range(n+1):
    for b in range(m+1):
        if a*b + (n-a)*(m-b) == k:
            flag = True
            break
    if flag:
        break

print('Yes' if flag else 'No')
