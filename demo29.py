"""
对jpeg格式图片的支持
"""
from tkinter import *
# 导入PIL模块
from PIL import Image, ImageTk
win = Tk()
# img = PhotoImage(file="WechatIMG6.jpeg")
# 读取文件
read_file = Image.open("WechatIMG6.jpeg")
img = ImageTk.PhotoImage(read_file)
Label(win, image=img).pack()
win.mainloop()
"""
错误提示
_tkinter.TclError: couldn't recognize data in image file "WechatIMG6.jpeg"
"""