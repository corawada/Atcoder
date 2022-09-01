new_alpha = input()

n = int(input())

mem = [input() for _ in range(n)]

def change_new_type(s):
    ans = ""
    for c in s:
        ans += chr(new_alpha.find(c) + ord('a'))
    return ans

def change_raw_type(s):
    ans = ""
    for c in s:
        ans += new_alpha[ord(c) - ord('a')]
    return ans

new_mem = list()
for m in mem:
    new_mem.append(change_new_type(m))

new_mem = sorted(new_mem)

for nm in new_mem:
    print(change_raw_type(nm))
