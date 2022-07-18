n = int(input())

def jadge(a, s):
    if (a==1) and (s==8):
        return True
    else:
        return False


for _ in range(n):
    a, s = map(int, input().split())
    print('Yes' if jadge(a, s) else 'No')
