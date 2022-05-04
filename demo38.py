"""
设置Text文本框组件
添加图片文字及按钮
"""
from tkinter import *
win = Tk()
# 设置多行文本框组件并赋值变量
text = Text(win, width=45, height=10, bg="#cae1ff", relief="solid")
# 创建图像并赋值变量
photo = PhotoImage(file="user.png")
# 调用方法在多行文本框中插入图片对象
text.image_create(END, image=photo)
# 调用方法在多行文本框中当前光标位置插入预设文本
text.insert(INSERT, "在这里添加文本：\n")
# 布局组件
text.pack()

# 设置Label组件，在多行文本框组件中放置标签组件
label = Label(win, padx=10, text="你点了我0下")
# 第三行的最后一个字符位置
text.window_create("3.end", window=label)

# 初始化变量值，定义函数
i = 0


def show():
    # 每次调用函数时，变量值+1
    global i
    i += 1
    label.config(text="你点了我\t" + str(i) + "下")


# 设置按钮组件，在多行文本框组件中赋值标签组件
btn = Button(win, text="你点我试试", command=show, padx=10)
# 第二行的最后一个字符位置
text.window_create("2.end", window=btn)

win.mainloop()
