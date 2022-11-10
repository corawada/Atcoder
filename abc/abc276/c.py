from itertools import permutations
n = int(input())

A = list(map(int, input().split()))

bikku = [1, ]

for i in range(2, n+1):
    bikku.append(bikku[-1] * i)

def seq_to_order(seq):
    remain = [1] * n
    res = 0

    for i, a in enumerate(seq):
        res += bikku[n-i-2] * (sum(remain[:a-1]))
        # print(bikku[n-i-2], sum(remain[:a-1]))
        remain[a-1] = 0

    return res + 1

def order_to_seq(order):
    order -= 1
    remain = [i+1 for i in range(n)] 
    ans_list = list()

    for i, b in enumerate(bikku[n-2::-1]):
        tar = order // b
        ans_list.append(remain.pop(tar))
        order %= b
    ans_list.append(remain.pop())
            
    return ans_list

ans = order_to_seq(seq_to_order(A)-1)


print(" ".join([str(a) for a in ans]))


