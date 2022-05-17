from collections import deque

n = int(input())
b = 998244353

nn = [1 for _ in range(11)]
nn[0] = 0
nn[10] = 0
nn = deque(nn)


for _ in range(n-1):
    tmp = deque()
    _, a1, a2, a3, a4, a5, a6, a7, a8, a9, __ = map(int, nn)
    nn = deque([0, (a1+a2)%b, (a1+a2+a3)%b, (a2+a3+a4)%b, (a3+a4+a5)%b, (a4+a5+a6)%b,
                 (a5+a6+a7)%b, (a6+a7+a8)%b, (a7+a8+a9)%b, (a8+a9)%b, 0])

ans = 0 
for _ in range(11):
    ans += nn.pop() 
ans = ans%998244353

print(ans)
    
    
