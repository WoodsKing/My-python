import tkinter

task = [
    '如果您没有安装点',
    '如果由于某种原因',
    '分布包含目录，您',
    '触发器完全无状态'
]


def show_day_task(day_task):
    day_task_number = len(day_task)
    day_Frame = tkinter.LabelFrame(top, bg='white', height=200, width=200, text='Day')
    day_Frame.place(x = 300,y=20)
    task_Frame = list()
    for i in range(day_task_number):
        task_Frame.append(tkinter.LabelFrame(day_Frame, bg='white', text='task'+str(i)))
        task_Frame[i].pack()


top = tkinter.Tk()
top.geometry("600x400")
top.title("manage")
top.configure(bg='white')
show_day_task(task)
top.mainloop()
