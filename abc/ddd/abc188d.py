from collections import defaultdict
n,k=map(int, input().split())
d=defaultdict(int)
for _ in range(n):
    a,b,c=map(int,input().split())
    d[a]+=c
    d[b+1]-=c
m = sorted(list(d.items()))
p,r,s=[0]*3
for x,u in m:
    s+=min(k,r)*(x-p)
    p=x
    r+=u
print(s)


