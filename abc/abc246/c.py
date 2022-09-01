n, k, x = map(int, input().split())

item = list(map(int, input().split()))

for idx, val in enumerate(item):
    if val >= x:
        if val//x > k: # クーポンの方が少ない
            item[idx] -= x*k
            k = 0
            break
        else:
            k -= val//x
            item[idx] -= x*(val//x)
else:
    item.sort()
    for i in range(min(len(item), k)):
        item.pop(-1)

ans = 0
for co in item:
    ans += co

print(ans)
    
