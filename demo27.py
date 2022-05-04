"""
在标签组件中添加图片
"""
from tkinter import *
win = Tk()
img = PhotoImage(file="1644560697.png")
Label(win, image=img).pack()
win.mainloop()
