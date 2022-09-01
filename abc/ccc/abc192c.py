n, k = map(int, input().split())


A = str(n)


for _ in range(k):
    sor = sorted(A)
    min_sort = int("".join(sor))
    max_sort = int("".join(sor[::-1]))
    A = str(max_sort - min_sort)

print(A)
