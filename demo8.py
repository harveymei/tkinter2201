# 设置组件边框样式，鼠标悬停组件上时的样式
from tkinter import *
win = Tk()
# 设置标签组件背景色，边框样式，鼠标悬停样式，宽与高
label = Label(win, bg="#63A4EB", relief="ridge", cursor="plus", width=30, height=2)
# 包装组件，设置宽高间距
label.pack(padx=5, pady=5, side=LEFT)
win.mainloop()
