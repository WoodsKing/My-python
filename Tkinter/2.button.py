import tkinter


def hit():
    ll = tkinter.Label(top, bg='red', width=10, height=10, text='我出来了')
    ll.pack()


top = tkinter.Tk()
top.title('button')
top.geometry('500x300')
b = tkinter.Button(top, text='点一点', width=10, height=1, command=hit)
b.pack()
top.mainloop()
