"""
纵向合并和横向合并
"""
from tkinter import *
win = Tk()
win.title("组件布局中基于行和列的合并")
# 设置标签组件赋值变量，设置组件宽高，组件边框样式，背景色
label = Label(win, text="横向合并4列", width=15, height=1, relief="groove", bg="#ede19a")
label21 = Label(win, text="横向合并2列", width=15, height=1, relief="groove", bg="#edbe9a")
label22 = Label(win, text="横向合并2列", width=15, height=1, relief="groove", bg="#edbe9a")
# 设置组件布局(行及列)，合并列
label.grid(row=0, column=0, columnspan=4)
label21.grid(row=1, column=0, columnspan=2)
label22.grid(row=1, column=2, columnspan=2)
# 设置第三行4个组件，布局组件
label31 = Label(win, width=15, height=1, relief="groove", bg="#e5aeae")
label31.grid(row=2, column=0)
label32 = Label(win, width=15, height=1, relief="groove", bg="#e5aeae")
label32.grid(row=2, column=1)
label33 = Label(win, width=15, height=1, relief="groove", bg="#e5aeae")
label33.grid(row=2, column=2)
label34 = Label(win, width=15, height=1, relief="groove", bg="#e5aeae")
label34.grid(row=2, column=3)
win.mainloop()
