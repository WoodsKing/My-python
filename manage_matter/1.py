from tkinter import *

root = Tk()

root.geometry('500x600')
Label(root, text="Label").pack()
frame1 = Frame(root, bg="purple").pack()
frame2 = Frame(frame1, bg='red')
frame2.pack(side=LEFT, padx=20)
frame3 = Frame(frame1, bg='yellow', highlightcolor="red")
frame3.pack(side=RIGHT, padx=100)
Label(frame2, text="我的世界").pack()
Label(frame2, text="魔兽争霸").pack()
Label(frame3, text="极品飞车22").pack()


root.mainloop()
