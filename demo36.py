"""
单行文本框组件的方法
使用delete()方法删除指定内容
"""
from tkinter import *
win = Tk()
# 设置单行文本框组件并赋值变量
op1 = Entry(win, relief="groove")
# 使用insert()方法插入预设文本
op1.insert(INSERT, "春风又绿江南岸")
# 布局组件
op1.grid(row=0)


# 定义函数
def back():
    # 使用get()方法获取字符并计算字符长度赋值变量
    length = len(op1.get())
    # 调用delete()方法删除最后一个字符
    op1.delete(length-1, END)


# 设置按钮组件，按钮事件为执调用back()函数，布局组件
Button(win, text="后退", command=back).grid(row=0, column=1)
win.mainloop()
