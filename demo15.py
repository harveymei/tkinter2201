
# 在窗口中显示斗兽棋游戏规则
from tkinter import *
win = Tk()
win.title("tkinter组件间距和组件内字符边距")
# 标签组件赋值变量
txt1 = Label(win, text="象吃狮", bg="#ba55d3", font=14)
txt2 = Label(win, text="狮吃虎", bg="#c1ffc1", font=14)
txt3 = Label(win, text="虎吃豹", bg="#cdb5cd", font=14)
txt4 = Label(win, text="豹吃狼", bg="#ba55d3", font=14)
txt5 = Label(win, text="狼吃狗", bg="#c1ffc1", font=14)
txt6 = Label(win, text="狗吃猫", bg="#cdb5cd", font=14)
txt7 = Label(win, text="猫吃鼠", bg="#ba55d3", font=14)
txt8 = Label(win, text="鼠吃象", bg="#c1ffc1", font=14)
# 包装组件，设置组件展示方式，设置组件水平及垂直间距，组件内字符边距
# txt1.pack(side="left", padx=10, pady=5, ipadx=6, ipady=4)
# txt2.pack(side="left", padx=10, pady=5, ipadx=6, ipady=4)
# txt3.pack(side="left", padx=10, pady=5, ipadx=6, ipady=4)
# txt4.pack(side="left", padx=10, pady=5, ipadx=6, ipady=4)
# txt5.pack(side="left", padx=10, pady=5, ipadx=6, ipady=4)
# txt6.pack(side="left", padx=10, pady=5, ipadx=6, ipady=4)
# txt7.pack(side="left", padx=10, pady=5, ipadx=6, ipady=4)
# txt8.pack(side="left", padx=10, pady=5, ipadx=6, ipady=4)
# 不再指定组件垂直间距和组件内字符垂直边距，指定组件纵向填充窗口，同时设置组件填充额外（水平）空间
txt1.pack(side="left", padx=10, ipadx=6, fill="y", expand=True)
txt2.pack(side="left", padx=10, ipadx=6, fill="y", expand=True)
txt3.pack(side="left", padx=10, ipadx=6, fill="y", expand=True)
txt4.pack(side="left", padx=10, ipadx=6, fill="y", expand=True)
txt5.pack(side="left", padx=10, ipadx=6, fill="y", expand=True)
txt6.pack(side="left", padx=10, ipadx=6, fill="y", expand=True)
txt7.pack(side="left", padx=10, ipadx=6, fill="y", expand=True)
txt8.pack(side="left", padx=10, ipadx=6, fill="y", expand=True)
win.mainloop()
