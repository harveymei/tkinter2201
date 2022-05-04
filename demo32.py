"""
单行文本框和密码
"""
from tkinter import *
win = Tk()
Label(win, text="密码", font=14).grid(row=0, column=0, pady=10)
Entry(win, show="#").grid(row=0, column=1)
win.mainloop()
