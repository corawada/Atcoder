q = int(input())


tutu = list()
for i in range(q):
    query = input().split()
    if query[0] == "1":
        for _ in range(int(query[2])):
            tutu.append(int(query[1]))
    else:
        ans = 0
        for j in range(int(query[1])):
            ans += tutu[j]
        print(ans)
        start = int(query[1])
        tutu = tutu[start:]


