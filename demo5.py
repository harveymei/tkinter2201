from tkinter import *

win = Tk()
win.title("tkinter基本属性")
# 设置窗口大小
win.geometry("300x150")
# 设置窗口背景颜色
win.configure(bg="yellow")
# 设置窗口最大尺寸
win.maxsize(500, 500)
# 定义一个字符串变量
couple = "\n\n上联：足不出户一台电脑打天下\n\n下联：窝宅在家一双巧手定乾坤\n\n横批：真我风采"
# 添加标签组件
txt = Label(win, text=couple, bg="yellow")
# 包装组件
txt.pack()
# 进入等待与处理窗口事件
win.mainloop()
