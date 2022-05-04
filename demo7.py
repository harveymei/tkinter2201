# 指定窗口大小以及文字样式
from tkinter import *
win = Tk()
win.geometry("300x200")
# 设置前景色，背景色，包装组件
# Label(win, text="小扣柴扉久不开", foreground="red", background="#C3DEEF").pack()
# 设置组件的宽高
# Label(win, text="小扣柴扉久不开", fg="red", bg="#C3DEEF", width=20, height=3).pack()
# 使用anchor设置文字在组件内的位置
# Label(win, text="小扣柴扉久不开", fg="red", bg="#C3DEEF", width=20, height=3, anchor="nw").pack()
# 使用padx和pady设置组件间距（文字距离组件边缘的间距）
# Label(win, text="小扣柴扉久不开", fg="red", bg="#C3DEEF", padx=20, pady=10).pack()
# 使用font设置组件字体
Label(win, text="小扣柴扉久不开", fg="red", bg="#C3DEEF", font="华文新魏 16 bold").pack()
win.mainloop()


