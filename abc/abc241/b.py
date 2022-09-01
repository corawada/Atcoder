n, m = map(int, input().split())
a = list(map(int, input().split()))
bn = list(map(int, input().split()))

for b in bn:
    if b in a:
        a.remove(b)
    else:
        print("No")
        break
else:
    print("Yes")
