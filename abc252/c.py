N = int(input())
ss = list()

def append_list(x):
    if x in next_time_list:
        append_list(x+10)
    else:
        next_time_list.append(x)

for _ in range(N):
    ss.append(input())

time = dict()
check_unique = list()
for i in range(10):
    time_list = list() 
    for j in range(N):
        time_list.append(ss[j].find(str(i)))
    time[i] = time_list
    if len(time_list) == len(set(time_list)):
        check_unique.append(i)
        
if len(check_unique) != 0:
    min_sec = 100
    for k in check_unique:
        if max(time[k]) < min_sec:
            min_sec = max(time[k])
    print(min_sec)
else:
    for dub in range(10):
        tmp_list = time[dub]
        next_time_list = list()
        for i in tmp_list:
            append_list(i)
        time[dub] = next_time_list
    min_sec = 100**100
    for k in range(10):
        if max(time[k]) < min_sec:
            min_sec = max(time[k])
    print(min_sec)
        



