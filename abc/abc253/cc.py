q = int(input())

num_dic = dict()

for _ in range(q):
    inp = list(map(int, input().split()))

    if inp[0] == 1:
        a = inp[1]
        if a in num_dic:
            num_dic[a] += 1
        else:
            num_dic[a] = 1

    elif inp[0] == 2:
        a = inp[1]
        b = inp[2]

        if a in num_dic:
            num_dic[a] -= b

            if num_dic[a] <= 0:
                del num_dic[a]

    elif inp[0] == 3:
        print(max(num_dic.keys()) - min(num_dic.keys()))
