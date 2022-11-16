n = int(input())

cards = set()

head = ["H", "D", "C" ,"S"]
tail = ['A', '2', '3', '4', '5', '6', '7', '8','9', 'T', 'J', 'Q', 'K']

for _ in range(n):
    s = input()
    if (s[0] in head) and (s[1] in tail):
        cards.add(s)
    else:
        print('No')
        break
else:
    if n == len(cards):
        print('Yes')
    else:
        print('No')
        



