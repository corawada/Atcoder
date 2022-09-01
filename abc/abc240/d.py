from collections import deque

n = int(input())

A = deque(map(int, input().split()))

tutu = [A.popleft(),]
tutu_n = [1,]

ans = [1,]
pre_ans = 1

print(1)

for _ in range(n-1):
    a = A.popleft()

    if not tutu:
        tutu.append(a)
        tutu_n.append(1)
        pre_ans += 1
    elif tutu[-1] == a:
        if tutu_n[-1] == a-1:
            tutu.pop()
            tutu_n.pop()
            pre_ans += -a + 1
        else:
            tutu_n[-1] += 1
            pre_ans += 1
    else:
        tutu.append(a)
        tutu_n.append(1)
        pre_ans += 1

    print(pre_ans)


