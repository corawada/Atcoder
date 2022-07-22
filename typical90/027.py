n = int(input())
member = set()
for i in range(1, n+1):
    s = input()
    if s in member:
        continue
    else:
        print(i)
        member.add(s)
