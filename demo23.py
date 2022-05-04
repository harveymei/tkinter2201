"""
使用place()方法布局组件
"""
from tkinter import *
win = Tk()
win.title("华容道")
win.geometry("240x300")
# 设置标签组件，赋值变量
txt1 = Label(win, text="赵云", bg="#93edd4", relief="groove", font=14)
txt2 = Label(win, text="曹操", bg="#a6e3a8", relief="groove", font=14)
txt3 = Label(win, text="黄忠", bg="#93edd4", relief="groove", font=14)
txt4 = Label(win, text="张飞", bg="#93edd4", relief="groove", font=14)
txt5 = Label(win, text="关羽", bg="#93edd4", relief="groove", font=14)
txt6 = Label(win, text="马超", bg="#93edd4", relief="groove", font=14)
txt7 = Label(win, text="卒", bg="#f3f5c4", relief="groove", font=14)
txt8 = Label(win, text="卒", bg="#f3f5c4", relief="groove", font=14)
txt9 = Label(win, text="卒", bg="#f3f5c4", relief="groove", font=14)
txt0 = Label(win, text="卒", bg="#f3f5c4", relief="groove", font=14)
# 布局组件，设置组件宽高，以及组件左上角坐标值
# txt1.place(width=60, height=120, x=0, y=0)
# txt2.place(width=120, height=120, x=60, y=0)
# txt3.place(width=60, height=120, x=180, y=0)
# txt4.place(width=60, height=120, x=0, y=120)
# txt5.place(width=120, height=60, x=60, y=120)
# txt6.place(width=60, height=120, x=180, y=120)
# txt7.place(width=60, height=60, x=60, y=180)
# txt8.place(width=60, height=60, x=120, y=180)
# txt9.place(width=60, height=60, x=0, y=240)
# txt0.place(width=60, height=60, x=180, y=240)
# 布局跟随窗口缩放（等比例缩放），组件大小为窗口大小的倍数
txt1.place(relwidth=0.25, relheight=0.4, relx=0, rely=0)
txt2.place(relwidth=0.5, relheight=0.4, relx=0.25, rely=0)
txt3.place(relwidth=0.25, relheight=0.4, relx=0.75, rely=0)
txt4.place(relwidth=0.25, relheight=0.4, relx=0, rely=0.4)
txt5.place(relwidth=0.5, relheight=0.2, relx=0.25, rely=0.4)
txt6.place(relwidth=0.25, relheight=0.4, relx=0.75, rely=0.4)
txt7.place(relwidth=0.25, relheight=0.2, relx=0.25, rely=0.6)
txt8.place(relwidth=0.25, relheight=0.2, relx=0.5, rely=0.6)
txt9.place(relwidth=0.25, relheight=0.2, relx=0, rely=0.8)
txt0.place(relwidth=0.25, relheight=0.2, relx=0.75, rely=0.8)

win.mainloop()
