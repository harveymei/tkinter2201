# 设置窗口大小及位置
from tkinter import *

win = Tk()
win.title("tkinter的窗口位置")
# 设置窗口属性，窗口背景颜色
win.configure(bg="#a7ea90")
# 定义窗口宽高变量
win_w = 300
win_h = 220
# 获取屏幕宽度及高度并赋值变量
scr_w = win.winfo_screenwidth()
scr_h = win.winfo_screenheight()
# 计算窗口水平和垂直位置并赋值变量
x = (scr_w - win_w) / 2
y = (scr_h - win_h) / 2
# 设置窗口大小和位置（格式化字符串传入参数）
# 窗口宽x窗口高+左上角x坐标值+左上角y坐标值
win.geometry("%dx%d+%d+%d" % (win_w, win_h, x, y))
# 定义字符串变量
strings = "\n\n程序员鄙视链\n\n一等码农搞算法，吃香喝辣调调参\n\n二等码农搞架构，高并低延能吹牛\n\n" \
          "三等码农搞工程，怼天怼地怼PM\n\n四等码农搞前端，浮层像素老黄牛"
# 添加标签组件
txt = Label(win, text=strings, bg="#a7ea90")
# 包装组件
txt.pack()
# 进入等待与处理窗口事件
win.mainloop()
