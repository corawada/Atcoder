I=sorted(list(input()));c=[I.pop(),I.pop()]
for i in range((len(I)//2)):c = [x+y for (x,y) in zip(sorted(c),[I.pop(),I.pop()])]
print(int(c[1]+I[0])*int(c[0]) if int(c[0]+I[0])*int(c[1])<int(c[1]+I[0])*int(c[0]) else int(c[0]+I[0])*int(c[1])) if len(I)%2!=0 else print(int(c[0])*int(c[1]))
