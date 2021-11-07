import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()


def prep(event):
    event.widget.config(bg='light blue')
    event.widget.bind('<Key>', edit)


def edit(event):
    print(event.char)


example = tk.Label(frame, text='Click me')
example.pack()
example.bind('<Button-1>', prep)
tk.mainloop()
