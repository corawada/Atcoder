import re
S = input()

chokudai = 'chokudai'

ans = 0
"""
def dfs(c, dep):
    global ans
    if c == 7:
        ans += S.count(chokudai[c], dep)
        return False

    lis = [m.start()+dep for m in re.finditer(chokudai[c], S[dep:])]
    # [(2, 4), (6, 8)]
    for i in lis:
        dfs(c+1, i+1)
dfs(0, 0)
print(ans)
"""

nn = []
chr_lis = {'c':[],
           'h':[],
           'o':[],
           'k':[],
           'u':[],
           'd':[],
           'a':[],
           'i':[]}
for idx, ch in enumerate(S):
    if ch in chokudai:
        chr_lis[ch].append(idx)


def dfs(c, dep):
    # print("call dfs --- tar:{} , dep={}".format(c, dep))
    global ans
    if c == 'c':
        ans += S.count('c', 0, dep)
        return False

    lis = list()
    for k in chr_lis[c]:
        if k < dep:
            lis.append(k)
        else:
            break


    for i in lis:
        dfs(chokudai[chokudai.find(c)-1], i)

dfs('i', len(S))
print(ans)
    
    


