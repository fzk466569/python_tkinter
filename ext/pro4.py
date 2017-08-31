from tkinter import *
# toplevel

root = Tk()


def create():
    top = Toplevel()
    top.attributes("-alpha", 0.5)
    top.title('fzk,fzk')

    msg = Message(top, text='sdaf')
    msg.pack()

button = Button(root, text='顶级窗口', command=create)
button.pack()

mainloop()
