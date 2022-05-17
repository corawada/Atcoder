S = list(input())
n, m = map(int, input().split())

nn = S[n-1]
mm = S[m-1]

S[n-1] = mm
S[m-1] = nn

print("".join(S))
