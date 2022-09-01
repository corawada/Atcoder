n = int(input())

def output_Sn(n):
    if n == 1:
        return "1"
    else:
        pre_sn = output_Sn(n-1)
        return "{sn} {num} {sn}".format(sn=pre_sn, num=n)

print(output_Sn(n))


