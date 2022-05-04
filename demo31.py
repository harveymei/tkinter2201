"""
单行文本框组件
"""
from tkinter import *
win = Tk()
# 设置标签组件，使用grid()方法设置组件坐标和纵向间距
Label(win, text="出发地：", font=14).grid(row=0, column=0, padx=10, pady=10)
# 设置单行文本框组件（位于上一组件右侧）
Entry(win).grid(row=0, column=1, padx=10)
# 设置标签组件
Label(win, text="目的地：", font=14).grid(row=1, column=0, padx=10, pady=10)
# 设置单行文本框组件（位于上一组件右侧）
Entry(win).grid(row=1, column=1, padx=10)
win.mainloop()
