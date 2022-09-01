input()
S = list(map(int, input().split()))

pre_s = []

for i in range(1, 150):
    for j in range(1, 150):
        pre_s.append(4*i*j + 3*(i+j))

ans = 0 
for s in S:
    if s not in pre_s:
        ans += 1

print(ans)
