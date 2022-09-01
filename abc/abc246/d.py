from math import ceil
n = int(input())

basis = ceil((n / 4 ) ** (1/3))
tmp_ans = 4 * (basis**3)

tmp_b = ceil(n**(1/3))
for a in range(basis+1):
    while True:
        value = a**3 + (a**2)*tmp_b + a*(tmp_b**2) + tmp_b**3
        if n <= value:
            tmp_b -= 1
            if tmp_b == -1:
                break
        else:
            tmp_b += 1
            value = a**3 + (a**2)*tmp_b + a*(tmp_b**2) + tmp_b**3
            break
    tmp_ans = min(tmp_ans, value)

print(tmp_ans)
    

