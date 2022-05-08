n = int(input())

item = list(map(int, input().split()))
item.sort()

for i in range(n+1):
    if i in item:
        continue
    else:
        print(i)
        break

