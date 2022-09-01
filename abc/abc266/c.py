from math import sqrt, acos
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

def calc_deg(x_lis, y_lis, z_lis):
    a_bac = [x_lis[0]-y_lis[0], x_lis[1]-y_lis[1]]
    b_bac = [z_lis[0]-y_lis[0], z_lis[1]-y_lis[1]]

    nai = b_bac[0]*a_bac[0] + a_bac[1]*b_bac[1]
    cosx = nai/(sqrt(a_bac[0]**2+a_bac[1]**2) * sqrt(b_bac[0]**2+b_bac[1]**2))

    print(cosx)
    print(acos(cosx))

calc_deg(a, b, c)
calc_deg(b, c, d)
calc_deg(c, d, a)
calc_deg(d, a, b)


print()
