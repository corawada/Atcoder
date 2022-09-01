#31760024
n,q = map(int,input().split())
fi=[0]
fn=[0]
for i in range(n):
    fi.append(i+1)
    fn.append(i+1)

for i in range(q):
    na = int(input())
    ib = fn[na]
    if ib!=n:
        nc = fi[ib+1]  
        fi[ib+1]=na
        fi[ib]=nc
        fn[na]=ib+1
        fn[nc]=ib
    else:
        nc = fi[ib-1]
        fi[ib-1]=na
        fi[ib]=nc
        fn[na]=ib-1
        fn[nc]=ib

ans = ""
for i in fi:
    if i==0:
        continue
    else:
        ans += str(i) + " "
print(ans)
