import tkinter,csv


def close(k):
    k.delete(tkinter.ACTIVE)

k = list()
with open('day_task.csv','r',encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        k.append(row)

print(k)
top = tkinter.Tk()
top.title("manage")
top.geometry("600x400")
top.configure(bg='white')

day_Frame = tkinter.LabelFrame(top, bg='white', text='Day')
day_Frame.place(x=50,y=50)

lb1 = tkinter.Listbox(day_Frame)
lb1.pack()

img = tkinter.PhotoImage(file='3.png')
bu = tkinter.Button(day_Frame,image=img,bg='white',width = 16,height=16,command=lambda x=lb1: close(x))


bu.pack()

for i in k:
    lb1.insert(0,i[1])


top.mainloop()
