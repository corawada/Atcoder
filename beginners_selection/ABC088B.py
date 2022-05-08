len_li = int(input())
li = list(map(int, input().split()))

sort_li = sorted(li)
ans = 0
for i in range(len_li):
    if i%2 == 0:
        ans += sort_li.pop(-1)
    else:
        ans -= sort_li.pop(-1)
print(ans)


