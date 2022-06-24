p = float(input())

def predict_time(x):
    seinou = 2 ** (x/1.5)
    return x + p/seinou

for i in range(0,100):
    if i == 0:
        vert = predict_time(0)
        continue
    next_v = predict_time(i)
    print("{} => {}".format(vert, next_v))
    if vert < next_v:
        break
    else:
        vert = next_v


