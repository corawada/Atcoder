mochi_len = int(input())

mochis = []

for i in range(mochi_len):
    mochis.append(int(input()))

print(len(set(mochis)))
