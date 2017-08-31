from tkinter import *

# scale 组件

root = Tk()
# 垂直
s1 = Scale(from_=0, to=50, tickinterval=5, resolution=5, length=200)
s1.pack()
# 水平
s2 = Scale(from_=0, to=500, orient=HORIZONTAL, length=600)
s2.pack()


def show():
    print(s1.get(), s2.get())

Button(root, text='获取位置', command=show).pack()

root.mainloop()
