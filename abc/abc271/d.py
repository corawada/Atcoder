n, s = map(int, input().split())

card_H = list()
card_T = list()
sum_dict = dict()
h, t = map(int, input().split())
sum_dict[h] = 'H'
sum_dict[t] = 'T'

for _ in range(n-1):
    h, t = map(int, input().split())
    card_H.append(h)
    card_T.append(t)


for ch, ct in zip(card_H, card_T):
    next_sum = dict()
    for key, value in sum_dict.items():
        next_sum[key+ch] = value + "H"
        next_sum[key+ct] = value + "T"

    sum_dict = next_sum

if s in sum_dict:
    print("Yes")
    print(sum_dict[s])
else:
    print("No")

    

