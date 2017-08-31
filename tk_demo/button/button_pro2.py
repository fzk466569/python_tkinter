from tkinter import *

root = Tk()


def commit():
    print(v.get())

v = IntVar()

Radiobutton(root, text='One', variable=v, value=1).pack(anchor='w')
Radiobutton(root, text='Two', variable=v, value=2).pack(anchor='w')
Radiobutton(root, text='Three', variable=v, value=3).pack(anchor='w')
Button(root, text='提交', command=commit).pack(anchor='w')

root.mainloop()