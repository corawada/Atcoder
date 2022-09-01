#31755692

N, Q = map(int,input().split())
a = list(map(int,input().split()))
dic = dict()
for i,j in zip(a,range(N)):
  if i not in dic:
    dic[i] = [j]
  else:
    dic[i].append(j)

print("len a: {}".format(len(a)))
print("N    : {}".format(N))
print(dic)

print("-----")

for i in range(Q):
  x,k = map(int,input().split())
  if x not in dic:
    print(-1)
  elif len(dic[x]) < k:
    print(-1)
  else:
    print(dic[x][k-1]+1)
