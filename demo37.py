"""
实现组件中数值的计算
"""
from tkinter import *
win = Tk()

# 设置一个单行文本框组件，并布局组件
op1 = Entry(win, width=5, relief="groove")
op1.grid(row=0, pady=20)
# 设置标签组件并布局组件
Label(win, text="+", bg="#f3e4a4").grid(row=0, column=1)
# 设置一个单行文本框组件，并布局组件
op2 = Entry(win, width=5, relief="groove")
op2.grid(row=0, column=2)
# 设置标签组件并布局组件
Label(win, text="=", bg="#f3e4a4").grid(row=0, column=3)
# 设置单行文本框组件并布局组件
result = Entry(win, width=5, relief="groove")
result.grid(row=0, column=4)


# 定义函数
def add():
    # 调用方法删除文本框中的所有字符
    result.delete(0, END)
    # 获取第一个文本框输入值转换为整数并赋值变量
    add1 = int(op1.get())
    # 获取第二个文本框输入值转换为整数并赋值变量
    add2 = int(op2.get())
    # 调用方法在结果文本框当前光标位置插入加法运算的值
    result.insert(INSERT, str(add1+add2))


# 设置按钮组件，定义点击后调用函数执行计算，布局组件
Button(win, text="计算", command=add, relief="groove", bg="#10c9f5").grid(row=1, columnspan=5, ipadx=10)
win.mainloop()
