input()
A = list(map(int, input().split()))

even_semi = 0
even_max = 0
odd_semi = 0
odd_max = 0

for tmp in A:
    if tmp % 2 == 0:
        if tmp > even_max:
            even_semi = even_max
            even_max = tmp
        elif tmp > even_semi:
            even_semi = tmp
    else:
        if tmp > odd_max:
            odd_semi = odd_max
            odd_max = tmp
        elif tmp > odd_semi:
            odd_semi = tmp

pre_ans = max(even_max+even_semi, odd_max+odd_semi)

if pre_ans % 2 == 0:
    print(pre_ans)
else:
    print(-1)


