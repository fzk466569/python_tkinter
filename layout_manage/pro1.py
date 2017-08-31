from tkinter import *

root = Tk()

Label(root, text='red', bg='red', fg='white').pack(fill=X, side=TOP)
Label(root, text='green', bg='green', fg='black').pack(fill=X, side=TOP)
Label(root, text='blue', bg='blue', fg='white').pack(fill=X, side=TOP)

mainloop()
