# 设置组件在窗口中的位置
from tkinter import *
win = Tk()
# 设置组件，并在包装组件时指定组件位置
# anchor设置组件在窗口下方，side设置组件从右向左排列
Label(win, text="下一步", bg="#8ebc90").pack(anchor="s", side="right", padx=10, pady=10)
win.mainloop()
