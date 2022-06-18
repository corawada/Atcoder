h1, h2, h3, w1, w2, w3 = map(int, input().split())


ans = 0
for i1 in range(1, h1-1):
    for j1 in range(1, h1-i1):
        k1 = h1-i1-j1

        for i2 in range(1, h2-1):
            for j2 in range(1, h2-i2):
                k2 = h2-i2-j2

                for i3 in range(1, h3-1):
                    for j3 in range(1, h3-i3):
                        k3 = h3-i3-j3


                        if (i1+i2+i3==w1) and (j1+j2+j3==w2) and (k1+k2+k3==w3): 
                            ans += 1

print(ans)
