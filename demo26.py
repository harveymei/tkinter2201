"""
↑ ↓ ← →
"""
from tkinter import *
win = Tk()
win.title("食物链")
# 动物标签组件赋值变量，设置标签文本，组件背景色，组件宽度，组件间距，字号
txt1 = Label(win, text="象", bg="#ffebcd", width=5, padx=4, pady=4, font=14)
txt2 = Label(win, text="狮", bg="#c1ffc1", width=5, padx=4, pady=4, font=14)
txt3 = Label(win, text="虎", bg="#ffebcd", width=5, padx=4, pady=4, font=14)
txt4 = Label(win, text="豹", bg="#c1ffc1", width=5, padx=4, pady=4, font=14)
txt5 = Label(win, text="狼", bg="#ffebcd", width=5, padx=4, pady=4, font=14)
txt6 = Label(win, text="狗", bg="#c1ffc1", width=5, padx=4, pady=4, font=14)
txt7 = Label(win, text="猫", bg="#ffebcd", width=5, padx=4, pady=4, font=14)
txt8 = Label(win, text="鼠", bg="#c1ffc1", width=5, padx=4, pady=4, font=14)
# 箭头标签组件赋值变量，设置标签文本，组件间距，前景色
# 使用grid()方法布局标签组件
txtr1 = Label(win, text="→", padx=2, pady=2, fg="#b22222")
txtr1.grid(row=1, column=2)
txtr2 = Label(win, text="→", padx=2, pady=2, fg="#b22222")
txtr2.grid(row=1, column=4)
txtb1 = Label(win, text="↓", padx=2, pady=2, fg="#b22222")
txtb1.grid(row=2, column=5)
txtb2 = Label(win, text="↓", padx=2, pady=2, fg="#b22222")
txtb2.grid(row=4, column=5)
txtl1 = Label(win, text="←", padx=2, pady=2, fg="#b22222")
txtl1.grid(row=5, column=4)
txtl2 = Label(win, text="←", padx=2, pady=2, fg="#b22222")
txtl2.grid(row=5, column=2)
txtt1 = Label(win, text="↑", padx=2, pady=2, fg="#b22222")
txtt1.grid(row=4, column=1)
txtt2 = Label(win, text="↑", padx=2, pady=2, fg="#b22222")
txtt2.grid(row=2, column=1)
# 坐标实际未从(0,0)开始，箭头标签组件坐标参照名称标签组件坐标设置
txt1.grid(row=1, column=1)
txt2.grid(row=1, column=3)
txt3.grid(row=1, column=5)
txt4.grid(row=3, column=5)
txt5.grid(row=5, column=5)
txt6.grid(row=5, column=3)
txt7.grid(row=5, column=1)
txt8.grid(row=3, column=1)
#
win.mainloop()
