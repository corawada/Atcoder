n, q = map(int, input().split())

load = {i:set() for i in range(n+1)}

for _ in range(n-1):
    a, b = map(int, input().split())
    load[a].add(b)
    load[b].add(a)


color_l = [False] * (n+1)
stack1 = {1, }
stack0 = set()

sude = set()
while stack1 or stack0:
    if stack1:
        tar = stack1.pop()
        color_l[tar] = 1
        for k in load[tar]:
            if k not in sude:
                sude.add(k)
                stack0.add(k)
    elif stack0:
        tar = stack0.pop()
        color_l[tar] = 0
        for k in load[tar]:
            if k not in sude:
                sude.add(k)
                stack1.add(k)

for _ in range(q):
    c, d = map(int, input().split())
    if color_l[c] == color_l[d]:
        print('Town')
    else:
        print('Road')

