N, K = map(int, input().split())
score = [sum(map(int, input().split())) for _ in range(N)]

border = sorted(score, reverse=True)[K-1] 

for i in score:
    if border <= i+300:
        print("Yes")
    else:
        print("No")
