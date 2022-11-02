from math import ceil

n = int(input())

f_ans = {0:1}

def f(n):
    if n in f_ans:
        return f_ans[n]

    else:
        ans = f(n//2) + f(n//3)
        f_ans[n] = ans
        return ans

print(f(n))

# for i, v in f_ans.items():
#     print(i, v)



