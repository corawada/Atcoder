n = int(input())

pascal = [1, 1]

for i in range(n):
    if i == 0:
        print(1)
    elif i == 1:
        print(1, 1)
    else:
        ne_pascal = [1]
        pascal.append(0)
        for idx, val in enumerate(pascal[:-1]):
            ne_pascal.append(val + pascal[idx+1])
        pascal = ne_pascal.copy()
        
        print(" ".join([str(k) for k in pascal]))
            

