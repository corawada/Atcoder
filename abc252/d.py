from random import randint

N = int(input())
A = list(map(int, input().split()))


print(N)
print(A)

# print(A)
ans = 0

def dfs(z, choice):
    global ans

   #  print("call: dfs({}, {})".format(z, choice))
    
    if len(choice) == 3:
        # print("choice")
        if len(choice) == len(set(choice)):
            # print("koko")
            ans += 1
            return False
        else:
            return False
    elif len(choice) > 3:
        return False

    if z == N:
        return False

    # 使わない
    if dfs(z+1, choice):
        return True

    # 使う
    choice_c = choice.copy()
    choice_c.append(A[z])
    if dfs(z+1, choice_c):
        return True

dfs(0, list())

print(ans)

    




