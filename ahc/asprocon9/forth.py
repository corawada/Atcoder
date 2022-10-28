from copy import deepcopy

class Order():
    weeks_val = 8
    machines_val = 10
    max_chenge_num = 2

    def __init__(self):
        self.weekday_num = 4
        self.holiday_num = 4
        self.success = False
        self.weekday_plan = list()
        self.holiday_plan = list()

    def rough_chenge_up(self):
        if self.weekday_num != 9:
            self.weekday_num += 1
        if self.holiday_num != 9:
            self.holiday_num += 1
        self.update_val()

    def rough_chenge_down(self):
        if self.weekday_num != 1:
            self.weekday_num -= 1
        if self.holiday_num != 1:
            self.holiday_num -= 1
        self.update_val()

    def update_val(self):
        self.weekday_plan = [str(self.weekday_num)*Order.weeks_val for _ in range(Order.machines_val)]
        self.holiday_plan = [str(self.holiday_num)*Order.weeks_val for _ in range(Order.machines_val)]

    def output(self):
        for weekday, holiday in zip(self.weekday_plan, self.holiday_plan):
            ans_str = ''
            for w, h in zip(weekday, holiday):
                ans_str += w + h
            print(ans_str)

x, m, c, e = map(int, input().split())
cost_aa = list()
cost_bb = list()
for i in range(m):
    tmp_a = list()
    tmp_b = list()
    for j in range(9):
        cost_a, cost_b = map(int, input().split())
        tmp_a.append(cost_a)
        tmp_b.append(cost_b)
    cost_aa.append(tmp_a)
    cost_bb.append(tmp_b)


Order.weeks_val = x
Order.machines_val = m
Order.max_chenge_num = c

ins_lis = [Order(), ]
ins_lis[-1].update_val()

for _ in range(e):
    # layer : output
    ins_lis[-1].output()

    # layer : input
    score, v, d = map(int, input().split())
    if d == 0:
        ins_lis[-1].success = True

    delay = [0 for _ in range(m)]
    load_count = [[] for _ in range(m)]
    for im in range(m):
        for _ in range(x):
            rd, ro = input().split()
            delay[im] += int(ro)
            load_count[im].append(rd=='0.000')

    ins_lis.append(deepcopy(ins_lis[-1]))
    if d != 0:
        ins_lis[-1].rough_chenge_up()
    else:
        ins_lis[-1].rough_chenge_down()



