N = int(input())

nn = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            dx1 = nn[j][0] - nn[i][0]
            dy1 = nn[j][1] - nn[i][1]
            dx2 = nn[k][0] - nn[i][0]
            dy2 = nn[k][1] - nn[i][1]
            if dx1 * dy2 != dx2 * dy1:
                ans += 1

print(ans)
