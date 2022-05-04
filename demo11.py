# 设置文字的排列方式
from tkinter import *
win = Tk()
# 字符串赋值变量
txt1 = "暮冬时烤雪"
txt2 = "迟夏写长信"
txt3 = "早春不过一棵树"
# 在pack()方法中通过side参数设置组件的展示方式
# Label(win, text=txt1, bg="#F5DFCC").pack(side="bottom")
# Label(win, text=txt2, bg="#EDB584").pack(side="bottom")
# Label(win, text=txt3, bg="#EF994C").pack(side="bottom")
# 设置标签组件的宽度为固定值（长度仍为默认），设置组件的水平间距为20，垂直间距为5
# Label(win, text=txt1, bg="#F5DFCC", width=20).pack(side="bottom", padx=20, pady=5)
# Label(win, text=txt2, bg="#EDB584", width=20).pack(side="bottom", padx=20, pady=5)
# Label(win, text=txt3, bg="#EF994C", width=20).pack(side="bottom", padx=20, pady=5)
# 设置组件内文字与组件边界的间距
Label(win, text=txt1, bg="#F5DFCC").pack(side="bottom", padx=20, pady=5, ipadx=10, ipady=5)
Label(win, text=txt2, bg="#EDB584").pack(side="bottom", padx=20, pady=5, ipadx=10, ipady=5)
Label(win, text=txt3, bg="#EF994C").pack(side="bottom", padx=20, pady=5, ipadx=10, ipady=5)
win.mainloop()
