"""
标签组件中的图片与文本布局
"""
from tkinter import *
win = Tk()
win.title("这里是标题")
# 设置窗口背景色
win.configure(bg="#eef3c3")
# 创建图片对象
img = PhotoImage(file="1644561360.jpg")
# 在标签组件中添加文字和图片，并设置图片于文字下方，设置字体字号，设置标签前景色与背景色
game = Label(win, text="欢乐写数字", image=img, compound="bottom", font="楷体 20 bold",
             fg="#d25eed", bg="#eef3c3")
# 使用grid()方法布局组件
game.grid(row=2, column=0, columnspan=2)
# 设置标签组件
Label(win, text="输入兑奖码领取稀有道具", bg="#eef3c3").grid(row=3, column=0, columnspan=2)
Label(win, text="兑奖码：", font=14, bg="#eef3c3").grid(row=4, column=0, sticky=E, pady=10)
# 设置标签组件（模拟输入框），宽度15，背景色为白色，设置边框样式，布局组件为上一组件右侧，设置组件纵向间距
Label(win, width=15, bg="#fff", relief="groove").grid(row=4, column=1, pady=10)
# 设置标签组件（模拟按钮）
Label(win, text="确认兑换", width=20, relief="groove", bg="#0996ed").grid(row=5, column=0, columnspan=2, pady=5)
win.mainloop()
