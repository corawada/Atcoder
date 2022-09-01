n = input()


l3 = (len(n)-1)//3
ans = 0
for i in range(l3-1):
    j = i +1
    ans += (10**3 * 10**(3*j) - 10**(3*j)) * j


ans += (int(n) - 10**(3*l3) + 1) * l3

print(ans)



