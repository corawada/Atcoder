import itertools

inp = input().split()

s = list(inp[0])

A = list(itertools.permutations(s))

B = ["".join(l) for l in A]
B = sorted(list(set(B)))

print(B[int(inp[1])-1])
