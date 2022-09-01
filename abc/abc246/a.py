
x = list()
y = list()
ans = ""

for _ in range(3):
    i, j = map(int, input().split())
    x.append(i)
    y.append(j)

for i in x:
    if x.count(i) == 1:
        ans += str(i)
        ans += " "

for i in y:
    if y.count(i) == 1:
        ans += str(i)

print(ans)
