"""
登录窗口和密码隐藏
"""
from tkinter import *
win = Tk()
# 设置窗口背景色
win.configure(bg="#efe5d2")
# 创建一个用户图片对象
user = PhotoImage(file="user.png")
# 创建一个密码图片对象
pwd = PhotoImage(file="password.png")
# 设置并布局标签组件，插入图片并设置标签背景色
Label(win, image=user, bg="#fff").grid(row=0)
# 设置并布局单行文本框组件，设置行和列坐标，以及横向及纵向组件间距
Entry(win).grid(row=0, column=1, padx=10, pady=10)
Label(win, image=pwd, bg="#fff").grid(row=1)
Entry(win, show="*").grid(row=1, column=1, padx=10, pady=10)
# 设置标签组件，添加文本，设置组件边框样式，布局组件，合并列，设置纵向组件间距
Label(win, text="确定", relief="groove").grid(row=2, columnspan=2, pady=10)
win.mainloop()
