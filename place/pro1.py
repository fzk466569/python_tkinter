from tkinter import *

root = Tk()
photo = PhotoImage(file='../tk_demo/18.gif')

Label(root, image=photo).pack()


def callback():
    print('中心')

Button(root, text='点我', command=callback).place(relx=0.5, rely=0.5, anchor=CENTER)

mainloop()
