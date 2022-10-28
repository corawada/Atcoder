n, m = map(int, input().split())

lis_n = [set() for _ in range(n+1)]

for _ in range(m):
    tmp_l = list(map(int, input().split()))[1:]
    while tmp_l:
        tar = tmp_l.pop()
        for l in tmp_l:
            lis_n[tar].add(l)
            lis_n[l].add(tar)

for tar_set in lis_n[1:]:
    if len(tar_set) != n-1:
        print('No')
        break
else:
    print('Yes')



