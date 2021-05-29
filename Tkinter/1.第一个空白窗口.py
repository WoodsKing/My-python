import tkinter

top = tkinter.Tk()
top.title("有文字的窗口")
top.geometry("500x300")
l = tkinter.Label(top,text='woodsking',bg='red',width=30,height=2)
l.pack()
top.mainloop()