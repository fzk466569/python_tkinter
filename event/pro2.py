from tkinter import *

root = Tk()


def callback(event):
    print('按下的字符：', event.keysym)

frame = Frame(root, width=500, height=300)
frame.bind('<Return>', callback)
frame.focus_set()
frame.pack()

root.mainloop()
