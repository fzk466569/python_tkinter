from tkinter import *

root = Tk()

e = Entry(root)
e.pack(padx=20, pady=20)

e.delete(0, END)
e.insert(0, '1111111')

root.mainloop()
