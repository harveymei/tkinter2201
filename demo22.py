"""
设置组件的缩放比例
"""
from tkinter import *
win = Tk()
# 设置窗口拉伸时，第一行组件的缩放比例为1（大小不变）
win.rowconfigure(0, weight=1)
# 设置窗口拉伸时，第二列组件的缩放比例为1（大小不变）
win.columnconfigure(0, weight=1)
# 设置标签组件宽高，组件边框样式，背景色
txt1 = Label(win, width=15, height=2, relief="groove", bg="#e0ffff")
# 设置组件布局，在窗口左上角，设置标签组件上对齐和左对齐
txt1.grid(row=0, column=0, sticky=N+W)
txt2 = Label(win, width=15, height=2, relief="groove", bg="#99ffcc")
# 设置组件布局，在窗口右上角，设置标签组件上对齐和右对齐
txt2.grid(row=0, column=1, sticky=N+E)
txt3 = Label(win, width=15, height=2, relief="groove", bg="#e0ffff")
# 设置组件布局，在窗口左下角，设置标签组件上对齐，下对齐和左对齐
txt3.grid(row=1, column=0, sticky=N+S+W)
txt4 = Label(win, width=15, height=2, relief="groove", bg="#99ffcc")
# 设置组件布局，在窗口右下角，设置标签组件上对齐，下对齐和右对齐
txt4.grid(row=1, column=1, sticky=N+S+E)
win.mainloop()
