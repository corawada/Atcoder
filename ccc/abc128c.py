n, m = map(int, input().split())


ranp_dic = dict()
for i in range(1, m+1):
    A = list(map(int, input().split()))
    ranp_dic[i] = A[1:]

P = list(map(int, input().split()))

# print(ranp_dic)
# print(P)

def jadge_on(bitstr):
    for key, value in ranp_dic.items():
        tmp_on = 0
        for v in value:
            if bitstr[v-1] == '1':
                tmp_on += 1
        if tmp_on % 2 == P[key-1]:
            continue
        else:
            return False
    else:
        return True

# bit 全探索
ans = 0
for bit in range(2**n):
    bitstr = "{bit:0{bitlen}b}".format(bit=bit, bitlen=n)
    if jadge_on(bitstr):
        # print(bitstr)
        ans += 1

print(ans)

