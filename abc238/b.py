n = int(input())

a = list(map(int, input().split()))

now_degree = 0
split = list()
split.append(0)
for i in a:
    now_degree = (now_degree+i) % 360
    split.append(now_degree)
    

max_div = 0
s = sorted(list(set(split)))

for j in range(len(s)-1):
    max_div = max(max_div, abs(s[j]-s[j+1]))

max_div = max(max_div, 360-s[-1])

print(max_div)


