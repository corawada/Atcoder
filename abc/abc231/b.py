tohyo = dict()

N = int(input())

for _ in range(N): 
    s = input()
    if s in tohyo:
        tohyo[s] += 1
    else:
        tohyo[s] = 1

print(max(tohyo, key=tohyo.get))
