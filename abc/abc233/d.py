# from pprint import pprint

n, k = map(int, input().split())
A = list(map(int,input().split()))

acc_A = [0,]

A_dic = dict()
A_dic[0] = [0,]

for idx, a in enumerate(A):
    tar = acc_A[-1] + a
    acc_A.append(tar)
    if tar in A_dic:
        A_dic[tar].append(idx+1) 
    else:
        A_dic[tar] = [idx+1,]

# print(acc_A)
# print(A_dic)

ans = 0
for r in range(1,n):
    sl = acc_A[r] - k
    if sl in A_dic:
        for l in A_dic[sl]:
            if l < r:
                ans += 1

print(ans)




