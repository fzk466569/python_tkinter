from tkinter import *

root = Tk()


def callback(event):
    print('鼠标位置：', event.x, event.y)

frame = Frame(root, width=500, height=300)
frame.bind('<Motion>', callback)
frame.focus_set()
frame.pack()

root.mainloop()
