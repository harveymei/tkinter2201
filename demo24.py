"""
Label组件基本使用
"""
from tkinter import *
win = Tk()
# 定义字符串赋值变量
strings = "\n上拜图灵只佑服务可用\n\n下跪关公但求永不宕机\n\n风调码顺"
# 设置标签组件，添加字符串，设置字符串最后一行左对齐（默认居中），字号，背景色
# 使用pack()方法布局组件，设置字符横向和纵向间距
Label(win, text=strings, justify="left", font=14, bg="#bfefea").pack(ipadx=10, ipady=5)
win.mainloop()
