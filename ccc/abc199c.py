N = int(input())
S = list(input())
Q = int(input())

s1 = S[0:N]
s2 = S[N:]

jun = True

for _ in range(Q):
    t, a, b = map(int, input().split())

    if t == 1:
        if jun:
            if a < b <= N:
                sa = s1[a-1]
                sb = s1[b-1]
                s1[b-1] = sa
                s1[a-1] = sb
            elif a <= N < b:
                sa = s1[a-1]
                sb = s2[b-1-N]
                s1[a-1] = sb
                s2[b-1-N] = sa
            else:  # N < a < b
                sa = s2[a-1-N]
                sb = s2[b-1-N]
                s2[a-1-N] = sb
                s2[b-1-N] = sa

        else:
            if a < b <= N:
                sb = s2[a-1]
                sa = s2[b-1]
                s2[b-1] = sb
                s2[a-1] = sa
            elif a <= N < b:
                sa = s2[a-1]
                sb = s1[b-1-N]
                s2[a-1] = sb
                s1[b-1-N] = sa
            else:  # N < a < b
                sa = s1[a-1-N]
                sb = s1[b-1-N]
                s1[a-1-N] = sb
                s1[b-1-N] = sa



    else:
        jun = not jun

if jun:
    print("".join(s1+s2))
else:
    print("".join(s2+s1))


