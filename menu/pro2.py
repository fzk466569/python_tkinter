from tkinter import *

root = Tk()


def hello():
    print('hello')

menubar = Menu(root)
menubar.add_command(label='撤销', command=hello)
menubar.add_command(label='重做', command=hello)

frame = Frame(root, width=512, height=512)
frame.pack()


def popup(event):
    menubar.post(event.x_root, event.y_root)

frame.bind("<Button-3>", popup)

root.mainloop()
