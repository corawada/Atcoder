N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())
"""
max(1−A,1−B)≤k≤min(N−A,N−B) をみたす全ての整数 k について、(A+k,B+k) を黒く塗る。
max(1−A,B−N)≤k≤min(N−A,B−1) をみたす全ての整数 k について、(A+k,B−k) を黒く塗る。
"""
k1 = (A+max(1-A, 1-B)) - (B+max(1-A, 1-B))
k2 = (A+max(1-A, B-N)) + (B-max(1-A, B-N))

"""
for i in range(P, Q+1):
    ans = ""
    for j in range(R, S+1):
        if (i - j == k1) or (i+j==k2):
            ans += '#'
        else:
            ans += '.'
    print(ans)
"""


for i in range(P, Q+1):
    j1 = min(S-R+2, max(0, i - k1 - R+1))
    if j1==S-R+2:
        j1 = 0
    j2 = min(S-R+2, max(0, k2 - i - R+1))
    if j2==S-R+2:
        j2 = 0
    J1 = min(j1, j2)
    J2 = max(j1, j2)

    if J1 == J2 == 0:
        print("."*(S-R+1))
    elif J1 == 0:
        print("."*(J2-1) + "#" + "."*(S-R+1-J2))
    elif J1 == J2:
        print("."*(J1-1) + "#" + "."*(S-R+1-J1))
    else:
        print('.'*(J1-1) + '#' + '.'*(J2-J1-1) + '#' + '.'*(S-R+1-J2))
