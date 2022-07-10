n = int(input())
A = list(map(int, input().split()))

ans = 10 ** 20
for bit in range(1 << (n-1)): #TODO
    # print(bit)
    tor = 0
    txor = 0
    for idx, a in enumerate(A):
        tor |= a

        if bit&(1 << idx):
            txor ^= tor
            tor = 0

    txor ^= tor
    ans = min(ans, txor)

print(ans)

# timestamp
# Data     Time     Diff     msg
# 22/07/09 10:48:48 00:00:00 rara
# 22/07/09 12:36:24 01:47:36 submit1
# 22/07/09 15:03:41 04:14:53 madamada
# 22/07/09 15:20:14 04:31:26 finish
