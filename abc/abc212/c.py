input()

A = sorted(list(set([int(i) for i in input().split()])))
B = sorted(list(set([int(i) for i in input().split()])))

diff = 10**100

def binary_serch(b):
    l = 0
    r = len(A)
    while r - l >= 1:
        i = (l+r) // 2
        if A[i] > b:
            r = i
        elif A[i] < b:
            l = i + 1
        else:
            return (0, 0, 0)
    return abs(b - A[i]), abs(b - A[i-1]), abs(b - A[(i+1)%len(A)])

    
for b in B:
    d1, d2, d3 = binary_serch(b)
    diff = min(diff, d1, d2, d3)

print(diff)



