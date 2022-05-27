A = [input() for _ in range(3)]
lis = ['ARC', 'AGC', 'AHC', 'ABC']

for a in A:
    lis.remove(a)

print(lis.pop())
