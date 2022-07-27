n = int(input())

# N <= 500
# C <= 100
# S <= 10**5
# F <= 100
# S % F == 0

station = list()
for _ in range(n-1):
    c, s, f = map(int, input().split())
    station.append([c, s, f])

station.append([0, 0, 1])
# print(station)

for idx, sta in enumerate(station):
    ans = sta[1] + sta[0]
    # print(sta, "-----")
    for nes in station[idx+1:]:
        # print(ans)
        if ans <= nes[1]:
            ans = nes[1] + nes[0]
        elif ans%nes[2] == 0:
            ans += nes[0]
        else:
            ans = nes[2] * (ans//nes[2] + 1) + nes[0]

    print(ans)

        

# timestamp
# Data     Time     Diff     msg
# 22/07/27 20:02:06 00:00:00 start
# 22/07/27 21:46:09 01:44:03 first
