abc = list(map(int, input().split()))

if sorted(abc)[1] == abc[1]:
    print("Yes")
else:
    print("No")
