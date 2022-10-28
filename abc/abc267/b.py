in_str = input()
line_bool = list()
line_bool.append(in_str[6]=='1')
line_bool.append(in_str[3]=='1')
line_bool.append((in_str[7]=='1') | (in_str[1]=='1'))
line_bool.append((in_str[4]=='1') | (in_str[0]=='1'))
line_bool.append((in_str[8]=='1') | (in_str[2]=='1'))
line_bool.append(in_str[5]=='1')
line_bool.append(in_str[9]=='1')

if in_str[0] == '1':
    print('No')
else:
    for idx, bo in enumerate(line_bool):
        if bo == False:
            if (True in line_bool[:idx]) and (True in line_bool[idx+1:]):
                print('Yes')
                break
    else:
        print('No')





# timestamp
# Data     Time     Diff     msg
# 22/09/14 19:59:02 00:00:00 
# 22/09/14 20:11:20 00:12:18 'finish'
# 22/09/14 20:42:29 00:43:27 second
