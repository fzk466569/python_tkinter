from tkinter import *

root = Tk()

Label(root, text='username:').grid(row=0, column=0, sticky=W)
Label(root, text='password:').grid(row=1, column=0, sticky=W)

Entry(root).grid(row=0, column=1)
Entry(root, show='*').grid(row=1, column=1)

mainloop()
