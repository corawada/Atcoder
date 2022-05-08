string = input()

while True:
    if string == "":
        print("YES")
        break

    elif string.endswith('dream'):
        string = string[:-5]
    elif string.endswith('dreamer'):
        string = string[:-7]
    elif string.endswith('erase'):
        string = string[:-5]
    elif string.endswith('eraser'):
        string = string[:-6]
    
    else:
        print("NO")
        break

