L, R = map(int, input().split())
S = input()

front = S[:L-1]
middle = S[L-1:R][::-1]
back = S[R:]


print(front, end="")
print(middle, end="")
print(back)
