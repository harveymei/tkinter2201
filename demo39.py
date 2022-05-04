"""
多行文本框组件Text的位置索引
"""
from tkinter import *
win = Tk()
# 设置组件赋值变量
text = Text(win)
# 插入文本
text.insert(INSERT, "I love python")
# 布局组件
text.pack()
# 控制台打印使用get()方法获取的位置上的字符
# 第1行第3列到第1行第7列
print(text.get(1.2, 1.6))
win.mainloop()

