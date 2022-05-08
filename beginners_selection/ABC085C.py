sheets_n, sum_value = map(int, input().split())

for fu in range(sheets_n + 1):
    for hi in range(sheets_n - fu + 1):
        if fu*10000 + hi*5000 + (sheets_n - fu - hi)*1000 == sum_value:
            print("{} {} {}".format(fu, hi, sheets_n-fu-hi))
            break
    else:
        continue
    break
else:
    print("-1 -1 -1")
            
