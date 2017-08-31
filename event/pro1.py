from tkinter import *

root = Tk()


def callback(event):
    print('111111111')
    print('点击位置：', event.x, event.y)

frame = Frame(root, width=500, height=300)
# <Control-shift-KeyPress-H> 同时按下control + shift + H
frame.bind('<Return>', callback)
frame.pack()

root.mainloop()
