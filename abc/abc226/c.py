N = int(input())

tt = dict()
time = dict() 


for k in range(N):
    inp = list(map(int, input().split()))
    tt[k+1] = inp[2:]
    time[k+1] = inp[0]

task_list = set(tt[N])
stack = task_list.copy()
    
ans = time[N]
while stack:
    p = stack.pop()
    tar = set(tt[p])
    ans += time[p]
    for i in tar:
        if i not in task_list:
            stack.add(i)
            task_list.add(i)
            
print(ans)
