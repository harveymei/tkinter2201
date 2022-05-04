# 模拟关闭窗口对话框
from tkinter import *
win = Tk()
# 设置窗口大小
win.geometry("350x150")
# 设置窗口标题
win.title("确认退出")
# 标签组件赋值变量
txt1 = Label(win, text="确定退出本窗口吗？")
txt2 = Label(win, text="果断退出", bg="#c1ffc1")
txt3 = Label(win, text="我再想想", bg="#cdb5cd")
# 包装组件，完全填充组件水平方向空间，设置组件间水平间距（由于未设置背景色，不易看出组件水平方向于窗口边框的间距）
txt1.pack(fill="x", padx=20)
# 包装组件，组件自右向左排序，设置组件水平间距和垂直间距，设置组件与窗口水平边距，设置组件位置于窗口右下角
# 实际显示的组件文字，从右到左依次是，“果断推出”，“我再想想”。
txt2.pack(side="right", padx=10, pady=20, ipadx=6, anchor="se")
txt3.pack(side="right", padx=10, pady=20, ipadx=6, anchor="se")
win.mainloop()
