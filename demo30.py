"""
在标签组件中指定文本换行位置
"""
from tkinter import *
win = Tk()
win.configure(bg="#c9edeb")
couple = "上联：足不出户一台电脑打天下下联：窝宅在家一双巧手定乾坤横批：真我风采"
# 标签组件赋值变量，设置组件背景色（与窗口背景色一致），字号，换行长度，末行左对齐
txt = Label(win, text=couple, bg="#c9edeb", font=14, wraplength=230, justify="left")
# 布局组件，设置组件横向和纵向间距
txt.pack(padx=20, pady=20)
win.mainloop()
