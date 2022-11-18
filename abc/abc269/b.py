nn = list()

flag = False
ans = [0, 0, 0, 0]
for i in range(10):
    s = input()
    nn.append(s)
    if not flag:
        if s.find('#') != -1:
            ans[0] = i + 1
            ans[2] = s.find('#') + 1
            ans[3] = s.rfind('#') + 1
            flag = True

for i in range(9, -1, -1):
    if nn[i].find('#') != -1:
        ans[1] = i + 1
        break


print(ans[0], ans[1])
print(ans[2], ans[3])

