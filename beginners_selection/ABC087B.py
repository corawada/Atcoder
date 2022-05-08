tmp_a = int(input()) # 500
tmp_b = int(input()) # 100
tmp_c = int(input())
target_price = int(input())

count = 0

max_a = min(target_price//500, tmp_a)

for i in range(max_a+1):
    balance_500 = target_price - 500*i
    # 100円と50円max出しても払えない
    if 100*tmp_b + 50*tmp_c < balance_500: 
        continue
    else:
        max_b = min(balance_500//100, tmp_b)

        for j in range(max_b+1):
            balance_100 = balance_500 -100*j
            # 50円max出しても払えない
            if 50*tmp_c < balance_100:
                continue
            else:
                if balance_100 % 50 == 0:
                    count += 1

print(count)
                
            
        
    
