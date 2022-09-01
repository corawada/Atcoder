n = int(input())
A = sorted(list(map(int, input().split())))

ans = A.pop()

for _ in range((n-2)//2):
    ans += A.pop() * 2

if n % 2 != 0:
    ans += A.pop()


print(ans)

