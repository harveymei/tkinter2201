"""
使用grid()方法布局组件
"""
from tkinter import *
win = Tk()
win.title("表格布局")
# 设置标签组件，使用grid()方法布局组件，设置组件间水平间距
Label(win, text="1*1=1", bg="#e0ffff").grid(row=0, column=0, padx=10)
Label(win, text="1*2=2", bg="#e0ffff").grid(row=1, column=0, padx=10)
Label(win, text="1*3=3", bg="#e0ffff").grid(row=2, column=0, padx=10)
Label(win, text="1*4=4", bg="#e0ffff").grid(row=3, column=0, padx=10)
Label(win, text="2*2=4", bg="#eea9b8").grid(row=1, column=1, padx=10)
Label(win, text="2*3=6", bg="#eea9b8").grid(row=2, column=1, padx=10)
Label(win, text="2*4=8", bg="#eea9b8").grid(row=3, column=1, padx=10)
Label(win, text="3*3=9", bg="#f08080").grid(row=2, column=2, padx=10)
Label(win, text="3*4=12", bg="#f08080").grid(row=3, column=2, padx=10)
Label(win, text="4*4=16", bg="#ffe1ff").grid(row=3, column=3, padx=10)
win.mainloop()
