num_dic = dict()

s_max = 0
s_min = 10**10

for _ in range(int(input())):
    inp = [int(i) for i in input().split()]

    if inp[0] == 1:
        a = inp[1]

        if a < s_min: s_min = a
        if a > s_max: s_max = a

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

                if s_max == a:
                    if num_dic:
                        s_max = max(num_dic.keys())
                    else:
                        s_max = 0

                if s_min == a:
                    if num_dic:
                        s_min = min(num_dic.keys())
                    else:
                        s_min = 10**10


    elif inp[0] == 3:
        print(s_max - s_min)
