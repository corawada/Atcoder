a, b = map(int, input().split())

s_list = list()
for i in range(97, 130):
    for _ in range(a):
        s_list.append(i)


print(chr(s_list[b-1]).upper())
