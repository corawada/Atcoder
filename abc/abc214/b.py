S, T = map(int, input().split())

ans = 0
for i in range(S+1):
    for j in range(max(0, S-i+1)):
        for k in range(max(0,S-i-j+1)):
            if i*j*k <= T:
                ans += 1

print(ans)
