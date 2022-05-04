# 在窗口中显示充值成功后获得的道具
from tkinter import *
win = Tk()
win.title("充值成功")
win.geometry("300x240")
# 字符串赋值变量
strings = "1、一级VIP30天\n\n2、每天额外赠送300金币7天\n\n3、全英雄限免30天\n"
# 标签组件赋值变量
text = Label(win, text="\n充值成功！", font="Times 18 bold")
# 包装组件
text.pack()
# 标签组件赋值变量
text_1 = Label(win, text="恭喜获得：\n", font=16)
# 包装组件并设置字符在组件中的位置（左侧，水平间距45像素）
text_1.pack(anchor=W, padx=45)
# 标签组件赋值变量，设置行对齐
text_2 = Label(win, text=strings, font=18, fg="red", justify="left")
text_2.pack()
win.mainloop()


