n = int(input())
A = list(map(int, input().split()))

gene = {1:0,}

for idx, a in enumerate(A):
    gene[2*(idx+1)] = gene[a] + 1
    gene[2*(idx+1)+1] = gene[a] + 1

for i in range(1, 2*(n+1)):
    print(gene[i])
    
