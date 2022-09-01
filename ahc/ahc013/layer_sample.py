import layer

n, k = map(int, input().split())
raw_nn = list()
for _ in range(n):
    raw_nn.append(list(input() + '9'))
raw_nn.append(list('9'*(n+1)))

print(layer.restricted_for_2(raw_nn, n, k))
