from tkinter import *

root = Tk()

options = ['one', 'two', 'three']

variable = StringVar()
# 设置默认值
variable.set('one')
w = OptionMenu(root, variable, *options)
w.pack()

root.mainloop()
