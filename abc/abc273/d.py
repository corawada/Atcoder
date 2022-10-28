from bisect import bisect_right, bisect_left

h, w, sr, sc = map(int, input().split())
n = int(input())

shougai_h = [set() for _ in range(h+1)]
shougai_w = [set() for _ in range(w+1)]

for _ in range(n):
    r, c = map(int, input().split())
    shougai_h[r].add(c)
    shougai_w[c].add(h)

bar_h = list()
bar_w = list()
for set_h in shougai_h:
    bar_h.append(sorted(set_h))
for set_w in shougai_w:
    bar_w.append(sorted(set_w))

q = int(input())
for _ in range(q):
    d, l = input().split()
    l = int(l)
    tar_l = sc-l
    if (d == 'L') or (d == 'R'):
        tar_bar = bar_h[sr]
        if d == 'L':
            ima_num = bisect_left(tar_bar, sc)
            tar_l = sc-l
            lo = 0
            hi = ima_num
            if lo == hi:
                sc = tar_l
            else:
                while lo != hi:
                    sak_num = bisect_left(tar_bar, tar_l, lo=lo, hi=hi)
                    if sak_num == ima_num:
                        hi = sak_num
                        tar_l = tar_bar[(lo+hi)//2]
                    else:
                        lo = sak_num
                        tar_l = tar_bar[(lo+hi)//2]
                sc = max(tar_bar[sak_num-1] + 1, 1)
        else:
            ima_num = bisect_right(tar_bar, sc)
            tar_l = sc+l
            lo = ima_num
            hi = len(tar_bar)
            if lo == hi:
                sc = tar_l
            else:
                while lo != hi:
                    sak_num = bisect_right(tar_bar, tar_l, lo=lo, hi=hi)
                    if sak_num == ima_num:
                        lo = sak_num
                        tar_l = tar_bar[(lo+hi)//2]
                    else:
                        hi = sak_num
                        tar_l = tar_bar[(lo+hi)//2]
                sc = min(tar_bar[sak_num] - 1, w)
    else:
        tar_bar = bar_w[sc]
        if d == 'U':
            ima_num = bisect_left(tar_bar, sr)
            tar_l = sr-l
            lo = 0
            hi = ima_num
            if lo == hi:
                sr = tar_l
            else:
                while lo != hi:
                    sak_num = bisect_left(tar_bar, tar_l, lo=lo, hi=hi)
                    if sak_num == ima_num:
                        hi = sak_num
                        tar_l = tar_bar[(lo+hi)//2]
                    else:
                        lo = sak_num
                        tar_l = tar_bar[(lo+hi)//2]
                sr = max(tar_bar[sak_num-1] + 1, 1)
        else:
            ima_num = bisect_right(tar_bar, sr)
            tar_l = sr+l
            lo = ima_num
            hi = len(tar_bar)
            if lo == hi:
                sr = tar_l
            else:
                while lo != hi:
                    sak_num = bisect_right(tar_bar, tar_l, lo=lo, hi=hi)
                    if sak_num == ima_num:
                        lo = sak_num
                        tar_l = tar_bar[(lo+hi)//2]
                    else:
                        hi = sak_num
                        tar_l = tar_bar[(lo+hi)//2]
                sc = min(tar_bar[sak_num] - 1, w)

    print(sr, sc)
        





