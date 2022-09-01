n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

itti = 0
sub_i = 0
for idx, val in enumerate(a):
    if val in b:
        if val == b[idx]:
            itti += 1
        else:
            sub_i += 1

print(itti)
print(sub_i)


    


