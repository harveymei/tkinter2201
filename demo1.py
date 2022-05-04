# 导入模块
from tkinter import *

# 实例化窗口
win = Tk()
# 添加窗口标题
win.title("demo")
# 添加按钮组件并设置样式
btn = Button(win, text="this is a button", font=14, relief="flat", bg="#00f5ff")
# 包装按钮
btn.pack(pady=20)
# 执行程序
win.mainloop()
