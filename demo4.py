# 为窗口添加标题
# 导入模块
from tkinter import *
# 实例化窗口
win = Tk()
# 设置窗口标题
win.title("tkinter basic")
# 添加标签组件
txt = Label(win, text="\n\ngame over\n\n")
# 包装组件
txt.pack()
# 进入等待与处理窗口事件
win.mainloop()
