# 使用fill参数设置组件填充所分配空间的方式
from tkinter import *
win = Tk()
# 字符串赋值变量
txt = "枯藤老树昏鸦，小桥流水人家。"
# 设置标签组件并赋值变量
txt1 = Label(win, text=txt, bg="#e6f5c8", fg="red", font=14)
# 包装组件并设置组件展示方式，填充组件垂直方向空间
txt1.pack(side="left", fill="y")
win.mainloop()
