import time


def binary_search(x):
    l = 0
    r = len(prime_nums) - 1
    while (r-l) > 1:
        print(r, l)
        time.sleep(1)
        i = (r + l)//2
        print("i --- {} : {}".format(i, prime_nums[i]))
        if x < prime_nums[i]:
            print(0)
            r = i
        elif x > prime_nums[i]:
            print(1)
            l = i
        else:
            l = i
            break
    return l

prime_nums = list(range(0, 100))

print(prime_nums)
print(binary_search(45))
