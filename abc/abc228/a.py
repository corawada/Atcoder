s, t, x = map(int, input().split())

if s > t :
    t += 24
  
if (s<=x) and (x<t):
    print("Yes")
elif (s<=x+24) and (x+24<t):
    print("Yes")
else:
    print("No")
