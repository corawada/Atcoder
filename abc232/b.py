def shift_char(s, n):
    return chr((ord(s) - 97 + n)%26 + 97)

S = input()
T = input()

diff = ord(T[0]) - ord(S[0])
ref = ""
for s in S:
    ref += shift_char(s, diff)


if T == ref:
    print("Yes")
else:
    print("No")
