"""
Entry单行文本框组件的方法
使用get()方法获取文本框中的内容
"""
from tkinter import *

win = Tk()
# 设置单行文本框组件赋值变量
entry = Entry(win)
# 布局组件
entry.grid(row=0)


# 定义函数，调用方法获取内容并打印内容
def show():
    strings = entry.get()
    print(strings)


# 设置按钮组件，调用函数，并布局组件
Button(win, text="显示", command=show).grid(row=0, column=1)
win.mainloop()
