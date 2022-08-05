for _ in range(int(input())):
    a,s=map(int,input().split());m = (s-(a*2)&a)
    print('No' if s<(a*2) else 'Yes' if m==0 else 'No')
