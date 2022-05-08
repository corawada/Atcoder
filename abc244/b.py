n = int(input())
t = str(input())

# kita = [0, 1]
# higa = [1, 0]
# mina = [0, -1]
# nisi = [-1, 0]
x = 0
y = 0
    
target = [1, 0]
for idx, val in enumerate(t):
    if val == "S":
        x += target[0]
        y += target[1]
    elif val == "R":
        if target[0] == 0:
            if target[1] == 1:
                target = [1, 0]
            else:
                target = [-1, 0]
        elif target[0] == 1:
            target = [0, -1]
        else:
            target = [0, 1]

print("{} {}".format(x, y))

    

