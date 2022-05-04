# 组件的公共方法
from tkinter import *
win = Tk()
label = Label(win, text="上拜图灵只佑服务可用\n\n下跪关公但求永不宕机\n\n风调码顺")
# 使用config()方法为组件配置参数
label.config(bg="#DEF1EF", fg="red", font=14)
label.pack()
win.mainloop()
