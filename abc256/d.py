n = int(input())

def jadge(start, tar_sec):
    if (start <= tar_sec <= sec_dict[start]) or \
            (tar_sec <= start <= sec_dict[tar_sec]):
                return True

    return False

def yugo(


sec_dict = dict()

for _ in range(n):
    start, end = map(int, input().split())
    if start in sec_dict:
        sec_dict[start] = max(sec_dict, end)
    else:
        sec_dict[start] = end

while True:
    for key, value in sec_dict.items():

        




print(ans)

    


