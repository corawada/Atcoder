n, m, k = map(int, input().split())

count = 0
def rec_count(kosu, max_v, threshould):
    global count
    if threshould<0: return 0
    for i in range(1, max_v):
        if i*kosu <= threshould:
            count += i**n
        else:
            rec_count(kosu-1, max_v, threshould-i)

rec_count(n, m+1, k)
    

print(count)


