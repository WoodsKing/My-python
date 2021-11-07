import tkinter

top = tkinter.Tk()
top.title("manage")
top.geometry("600x400")
top.configure(bg='white')

frame = tkinter.Frame(top, width=384, height=512)
frame.place(x=10, y=0)

vbar = tkinter.Scrollbar(frame, orient=tkinter.VERTICAL)
vbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

canvas = tkinter.Canvas(frame, bg='white', width=200, height=200, scrollregion=(0, 0, 200, 1020),
                        yscrollcommand=vbar.set)  # 创建canvas
canvas.pack(fill=tkinter.BOTH)
frame1 = tkinter.LabelFrame(canvas, bg='white', width=200, height=200, text='day')

vbar.configure(command=canvas.yview)

img = tkinter.PhotoImage(file='3.png')

li = list()
day = list()
bu = list()
for i in range(5):
    day.append(tkinter.Frame(frame1, bg='white'))

    if i % 2 == 0:
        li.append(tkinter.Label(day[i], width=20, height=1, text="物", bg='#81D8CF'))
        li[i].pack(side=tkinter.LEFT, padx=10)
    else:
        li.append(tkinter.Label(day[i], width=20, height=1, text='物', bg='#002ea5',fg='white'))
        li[i].pack(side=tkinter.LEFT, padx=10)
    bu.append(tkinter.Button(day[i],image=img, width=16, height=16,bg = 'white'))
    bu[i].pack(side=tkinter.LEFT, padx=10)
    day[i].pack(side=tkinter.TOP, pady=5)

canvas.create_window((100, 0), window=frame1, anchor='n')
canvas.config(yscrollcommand=vbar.set)  # 设置
top.mainloop()
