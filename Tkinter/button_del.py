"""
@Author : 行初心
@Date   : 18-10-1
@Blog   : www.cnblogs.com/xingchuxin
@Gitee  : gitee.com/zhichengjiu
"""
from tkinter import *
def main():
    root = Tk()
    my_lb = Listbox(root)
    my_lb.pack()
    my_list = ["北斗星", "贪狼", "巨门", "禄存", "文曲", "廉贞", "武曲", "破军", "左辅", "右弼"]
    for item in my_list:
        my_lb.insert(END, item)
    b = Button(root,
           text='删除选中内容',
           command=lambda x=my_lb: x.delete(ACTIVE)
           )
    # 在初始状态下，不选择的话，默认删除第一个
    b.pack()
    mainloop()
if __name__ == '__main__':
    main()