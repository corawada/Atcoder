from bisect import bisect
N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = list()

score = list()
idx = 1
for a, b in zip(A, B):
    score.append([a, b, a+b, idx])
    idx += 1

sorted_a = sorted(score, key=lambda x:(x[0], -x[3]))
for _ in range(X):
    ans.append(sorted_a.pop()[3])


sorted_b = sorted(sorted_a, key=lambda x:(x[1], -x[3]))
for _ in range(Y):
    ans.append(sorted_b.pop()[3])

sorted_c = sorted(sorted_b, key=lambda x:(x[2], -x[3]))
for _ in range(Z):
    ans.append(sorted_c.pop()[3])

ans = sorted(ans)

for an in ans:
    print(an)
