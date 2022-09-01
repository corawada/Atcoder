s = input()


s.islower()
s.isupper()

if (not s.islower()) and (not s.isupper()) and (len(s) == len(set(s))):
    print("Yes")
else:
    print("No")

