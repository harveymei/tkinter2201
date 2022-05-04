# 导入模块，使用ttk模块中的组件样式覆盖tkinter模块中的组件样式
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

# 实例化窗口
root = Tk()
# 设置窗口标题
root.title("ttk demo")
#
style = Style()
# 通过style()方法设置组件样式
style.configure("TButton", font=14, relief="flat", background="#00f5ff")
btn = ttk.Button(text="this is a button", style="TButton")
btn.pack(pady=20)
root.mainloop()
