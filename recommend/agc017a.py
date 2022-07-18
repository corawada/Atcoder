nCr = {}
def cmb(n, r):
    if r == 0 or r == n: return 1
    if r == 1: return n
    if (n,r) in nCr: return nCr[(n,r)]
    nCr[(n,r)] = cmb(n-1,r) + cmb(n-1,r-1)
    return nCr[(n,r)]

n, p = map(int, input().split())
A = [i%2 for i in list(map(int, input().split()))]

odd = 0
even = 0

for a in A:
    if a == 0:
        even += 1
    else:
        odd += 1

even_tori = 2**even

ans = 0
if p == 1:
    for i in range(1, ((odd+1)//2)*2, 2):
        ans += cmb(odd, i)
else:
    for i in range(0, (odd//2)*2+1, 2):
        ans += cmb(odd, i)

ans = ans * even_tori

print(ans)



