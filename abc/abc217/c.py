s = [0]*int(input())
for idx, val in enumerate([int(i) for i in input().split()]):
    s[val-1] = str(idx+1)

print(" ".join(s))
