s = input()

b = set("0123456789")

for i in s:
    b.remove(i)

print(b.pop())
