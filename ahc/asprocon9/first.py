x, m, c, e = map(int, input().split())

for _ in range(m*9):
    input()


const_list = [4 for _ in range(m)]
for _ in range(e):
    
    for i in range(m):
        print(str(const_list[i])*(2*x))

    score, v, d = map(int, input().split())
    delay = [0 for _ in range(m)]
    for im in range(m):
        for _ in range(x):
            rd, ro = input().split()
            delay[im] += int(ro)

    for idx, value in enumerate(delay):
        if value:
            const_list[idx] += 1







