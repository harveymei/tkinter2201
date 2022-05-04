"""
Entry单行文本框组件方法
insert()方法
文本框中的默认文本
"""
from tkinter import *
win = Tk()
# 设置标签组件并布局
Label(win, text="用户名：").grid(row=0, column=0)
# 设置单行文本框组件并赋值变量
entry = Entry(win, relief="groove")
# 调用方法在指定位置插入字符串
entry.insert(0, "admin")
# 布局组件
entry.grid(row=0, column=1)
win.mainloop()
