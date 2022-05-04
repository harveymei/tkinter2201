"""
使用sticky控制组件对齐
"""
from tkinter import *
win = Tk()
# 设置标签组件，背景色，边框样式，布局。
Label(win, text="春花秋月何时了", bg="#ebc7c7", relief="groove").grid(row=0, column=0)
# 组件与上一组件默认为居中对齐。
# Label(win, text="往事知多少", bg="#dfc7eb", relief="groove").grid(row=1, column=0)
# 修改组件为左对齐
# Label(win, text="往事知多少", bg="#dfc7eb", relief="groove").grid(row=1, column=0, sticky=W)
# 修改组件为左右拉伸对齐
Label(win, text="往事知多少", bg="#dfc7eb", relief="groove").grid(row=1, column=0, sticky=W+E)
win.mainloop()
