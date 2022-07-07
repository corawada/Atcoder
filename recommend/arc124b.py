# おまじない
import sys
sys.setrecursionlimit(10000)

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# print(n)
# print(A)
# print(B)

def dfs(idx_a, unused_list):
    if unused_list:
        for b in unused_list:
            if A[idx_a] ^ b == xor_num:
                next_unused = unused_list.copy()
                next_unused.remove(b)
                if dfs(idx_a+1, next_unused):
                    return True
        else:
            return False
    else:
        return True

ans_list = set()
for idx, b in enumerate(B):
    # print('-'*30)
    xor_num = A[0] ^ b
    unused_list = B.copy()
    unused_list.remove(b)
    # print("xor : {}   , unused : {}".format(xor_num, unused_list))
    if dfs(1, unused_list):
        ans_list.add(xor_num)


print(len(ans_list))
for i in sorted(list(ans_list)):
    print(i)
