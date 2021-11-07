import tkinter as tk
import tkinter.font as tf
import csv

l1 = [['10', '比如在今年5月份', '0'], ['2', '认识了北斗九星', '1']]
l2 = [['2', '古人却称之为北斗九星呢？', '0'], ['2', '数千年前还很明亮', '2']]
l3 = [['3', '相比于其他7颗星辰', '0'], ['2', '九星被认为是北斗九', '3']]


class SaveCSV:

    def __init__(self):
        self.day = 'day'
        self.week = 'week'
        self.month = 'month'

    def red(self):
        task = {
            self.day: '',
            self.week: '',
            self.month: ''
        }
        # 读取每天数据
        k = list()
        with open(self.day + '.csv', 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                k.append(row)
        task[self.day] = k
        # 读取每周数据
        k = []
        with open(self.week + '.csv', 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                k.append(row)
        task[self.week] = k
        k = []
        with open(self.month + '.csv', 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                k.append(row)
        task[self.month] = k
        return task

    def writ(self, select, data):
        if select == self.day:
            with open(self.day + '.csv', 'w', encoding='utf-8', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(data)
        if select == self.week:
            with open(self.week + '.csv', 'w', encoding='utf-8', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(data)
        if select == self.month:
            with open(self.month + '.csv', 'w', encoding='utf-8', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(data)


class Windows:
    def __init__(self):
        self.cs = SaveCSV()
        self.task = self.cs.red()
        self.top = tk.Tk()
        self.day_task = self.task['day']
        self.week_task = self.task['week']
        self.month_task = self.task['month']
        self.fnot_title = tf.Font(family='楷体', size=20, weight=tf.BOLD,slant=tf.ITALIC)
        self.finishfont = tf.Font(family='楷体',overstrike=1,size=10)
        self.img = tk.PhotoImage(file='1.png')
        self.lab_list = {
            'day':list(),
            'week':list(),
            'month':list()
        }
        self.DayStyle = {
            'canvas_Frame': 'white',  # 画布框架颜色
            'canvas': 'white',  # 画布颜色
            'task_frame': 'white',  # 任务框架颜色
            'lab_list': 'white',  # 标签列表颜色
            'Y_task_fg': '#A9A9A9',  # 任务前景颜色未完成
            'Y_task_bg': '#D3ECFD',  # 任务背景颜色未完成
            'N_task_fg': '#000000',  # 任务前景颜色完成
            'N_task_bg': '#40ADF6'  # 任务背景颜色完成
        }
    def update(self,datindex):
        if datindex[0] == 'day':
            self.day_task[datindex[1]][2] = 1
            self.cs.writ(datindex[0], self.day_task)
        if datindex[0] == 'week':
            self.week_task[datindex[1]][2] = 1
            self.cs.writ(datindex[0], self.week_task)
        if datindex[0] == 'month':
            self.month_task[datindex[1]][2] = 1
            self.cs.writ(datindex[0], self.month_task)
    def set_windows(self):
        self.top.geometry("600x600")  # 设置窗口大小
        self.top.title("manage")  # 设置窗口标题
        self.top.configure(bg='white')  # 设置窗口背景
        # self.top.wm_attributes('-topmost',1)
    def getindex(self,widget):
        for i in range(len(self.lab_list['day'])):
            if widget is self.lab_list['day'][i]:
                return ['day', i]
        for i in range(len(self.lab_list['week'])):
            if widget is self.lab_list['week'][i]:
                return ['week', i]
        for i in range(len(self.lab_list['month'])):
            if widget is self.lab_list['month'][i]:
                return ['month', i]
    def finish(self,event):
        event.widget.config(bg=self.DayStyle['Y_task_bg'], fg=self.DayStyle['Y_task_fg'],font=self.finishfont)
        k = self.getindex(event.widget)
        print(k[0])
        self.update(k)

    def run(self):
        self.set_windows()
        self.saying()
        self.show_day()
        self.show_line()
        self.show_week()
        self.show_month()
        tk.mainloop()
    def saying(self):
        saying = tk.Label(self.top, text='天下虽安，忘站必危',bg='white', fg='#ff8a00',font=self.fnot_title)
        saying.pack(side=tk.TOP,fill=tk.X)
    def show_line(self):
        line1 = tk.Label(self.top, bitmap="gray50", width=250, height=1, bg='#1A92F9', fg='#1A92F9')
        line1.pack(side=tk.TOP, fill=tk.X, pady=10)


    def show_day(self):
        # 创建画布框架并放置
        day_canvas_Frame = tk.Frame(self.top, bg=self.DayStyle['canvas_Frame'])
        day_canvas_Frame.pack(side=tk.TOP, anchor='ne', padx=10, pady=5)

        # 创建滚动条
        day_vbar = tk.Scrollbar(day_canvas_Frame, orient=tk.VERTICAL)
        day_vbar.pack(side=tk.RIGHT, fill=tk.Y)
        # 创建canvas画布
        day_canvas = tk.Canvas(day_canvas_Frame, bg=self.DayStyle['canvas'], width=250, height=200,
                               scrollregion=(0, 0, 250, 1020),
                               yscrollcommand=day_vbar.set)
        day_canvas.pack(fill=tk.BOTH)
        # 创建任务框架
        day_task_frame = tk.LabelFrame(day_canvas, bg=self.DayStyle['task_frame'], text='day')
        # 更新滚动条配置
        day_vbar.configure(command=day_canvas.yview)
        # 将day_task_frame放在画布上
        day_canvas.create_window((0, 0), window=day_task_frame, anchor='nw')
        # 更新画布设置
        day_canvas.config(yscrollcommand=day_vbar.set)  # 设置
        # 每日任务框架列表
        day_task_num = list()
        # 按键列表
        # day_bu = list()
        # 标签列表
        day_lab_list = self.lab_list['day']
        for i in range(len(self.day_task)):
            day_task_num.append(tk.Frame(day_task_frame, bg=self.DayStyle['lab_list']))
            day_task_num[i].pack(side=tk.TOP, pady=5)

            if self.day_task[i][2] == '0':
                day_lab_list.append(
                    tk.Label(day_task_num[i], bg=self.DayStyle['N_task_bg'], fg=self.DayStyle['N_task_fg'], width=30,
                             height=1, text=self.day_task[i][1]))
                day_lab_list[i].pack(side=tk.LEFT, padx=10)
                day_lab_list[i].bind('<Button-1>',self.finish)
            else:
                day_lab_list.append(
                    tk.Label(day_task_num[i], bg=self.DayStyle['Y_task_bg'], fg=self.DayStyle['Y_task_fg'], width=30,
                             height=1, text=self.day_task[i][1],font=self.finishfont))
                day_lab_list[i].pack(side=tk.LEFT, padx=10)
            # day_bu.append(tk.Button(day_task_num[i], image=self.img, width=16, height=16, bg=self.DayStyle['lab_list']))
            # day_bu[i].pack(side=tk.LEFT, padx=10)
            day_task_num[i].pack(side=tk.TOP, pady=5)

    def show_week(self):
        # 创建画布框架并放置
        week_canvas_Frame = tk.Frame(self.top, bg=self.DayStyle['canvas_Frame'])
        week_canvas_Frame.pack(side=tk.RIGHT, anchor='ne', padx=10)
        # 创建滚动条
        week_vbar = tk.Scrollbar(week_canvas_Frame, orient=tk.VERTICAL)
        week_vbar.pack(side=tk.RIGHT, fill=tk.Y)
        # 创建canvas画布
        week_canvas = tk.Canvas(week_canvas_Frame, bg=self.DayStyle['canvas'], width=250, height=200,
                                scrollregion=(0, 0, 250, 1020),
                                yscrollcommand=week_vbar.set)
        week_canvas.pack(fill=tk.BOTH)
        # 创建任务框架
        week_task_frame = tk.LabelFrame(week_canvas, bg=self.DayStyle['task_frame'], text='week')
        # 更新滚动条配置
        week_vbar.configure(command=week_canvas.yview)
        # 将week_task_frame放在画布上
        week_canvas.create_window((0, 0), window=week_task_frame, anchor='nw')
        # 更新画布设置
        week_canvas.config(yscrollcommand=week_vbar.set)  # 设置
        # 每周任务框架列表
        week_task_num = list()
        # 按键列表
        # week_bu = list()
        # 标签列表
        week_lab_list = self.lab_list['week']
        for i in range(len(self.week_task)):
            week_task_num.append(tk.Frame(week_task_frame, bg=self.DayStyle['lab_list']))
            week_task_num[i].pack(side=tk.TOP, pady=5)
            if self.week_task[i][2] == '0':
                week_lab_list.append(
                    tk.Label(week_task_num[i], bg=self.DayStyle['N_task_bg'], fg=self.DayStyle['N_task_fg'], width=25,
                             height=1, text=self.week_task[i][1]))
                week_lab_list[i].pack(side=tk.LEFT, padx=10)
                week_lab_list[i].bind('<Button-1>', self.finish)
            else:
                week_lab_list.append(
                    tk.Label(week_task_num[i], bg=self.DayStyle['Y_task_bg'], fg=self.DayStyle['Y_task_fg'], width=25,
                             height=1, text=self.week_task[i][1],font=self.finishfont))
                week_lab_list[i].pack(side=tk.LEFT, padx=10)
            # week_bu.append(
            #     tk.Button(week_task_num[i], image=self.img, width=16, height=16, bg=self.DayStyle['lab_list']))
            #  week_bu[i].pack(side=tk.LEFT, padx=10)
            week_task_num[i].pack(side=tk.TOP, pady=5)

    def show_month(self):
        # 创建画布框架并放置
        month_canvas_Frame = tk.Frame(self.top, bg=self.DayStyle['canvas_Frame'])
        month_canvas_Frame.pack(side=tk.RIGHT, anchor='ne', padx=10)
        # 创建滚动条
        month_vbar = tk.Scrollbar(month_canvas_Frame, orient=tk.VERTICAL)
        month_vbar.pack(side=tk.RIGHT, fill=tk.Y)
        # 创建canvas画布
        month_canvas = tk.Canvas(month_canvas_Frame, bg=self.DayStyle['canvas'], width=290, height=200,
                                 scrollregion=(0, 0, 290, 1020),
                                 yscrollcommand=month_vbar.set)
        month_canvas.pack(fill=tk.BOTH)
        # 创建任务框架
        month_task_frame = tk.LabelFrame(month_canvas, bg=self.DayStyle['task_frame'], text='month')
        # 更新滚动条配置
        month_vbar.configure(command=month_canvas.yview)
        # 将month_task_frame放在画布上
        month_canvas.create_window((0, 0), window=month_task_frame, anchor='nw')
        # 更新画布设置
        month_canvas.config(yscrollcommand=month_vbar.set)  # 设置
        # 每周任务框架列表
        month_task_num = list()
        # 按键列表
        # month_bu = list()
        # 标签列表
        month_lab_list = self.lab_list['month']
        for i in range(len(self.month_task)):
            month_task_num.append(tk.Frame(month_task_frame, bg=self.DayStyle['lab_list']))
            month_task_num[i].pack(side=tk.TOP, pady=5)

            if self.month_task[i][2] == '0':
                month_lab_list.append(
                    tk.Label(month_task_num[i], bg=self.DayStyle['N_task_bg'], fg=self.DayStyle['N_task_fg'], width=30,
                             height=1, text=self.month_task[i][1]))
                month_lab_list[i].pack(side=tk.LEFT, padx=10)
                month_lab_list[i].bind('<Button-1>', self.finish)
            else:
                month_lab_list.append(
                    tk.Label(month_task_num[i], bg=self.DayStyle['Y_task_bg'], fg=self.DayStyle['Y_task_fg'], width=30,
                             height=1, text=self.month_task[i][1],font=self.finishfont))
                month_lab_list[i].pack(side=tk.LEFT, padx=10)
            # month_bu.append(
            #     tk.Button(month_task_num[i], image=self.img, width=16, height=16, bg=self.DayStyle['lab_list']))
            # month_bu[i].pack(side=tk.LEFT, padx=10)
            month_task_num[i].pack(side=tk.TOP, pady=5)


win = Windows()
win.run()
