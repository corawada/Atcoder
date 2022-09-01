l = list()
l.append(input())
l.append(input())
l.append(input())

T = list(input())

ans = ""
for i in T:
    ans += l[int(i)-1]

print(ans)

