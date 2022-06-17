n = int(input())

non_exs = set()
aru_exs = set()

for _ in range(n):
    s = input()
    if s[0] == '!':
        aru_exs.add(s[1:])
    else:
        non_exs.add(s)

for i in aru_exs:
    if i in non_exs:
        print(i)
        break
else:
    print('satisfiable')
