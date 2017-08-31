from tkinter import *

root = Tk()

sb = Scrollbar(root)
sb.pack(side=RIGHT, fill=Y)

lb = Listbox(root, yscrollcommand=sb.set)

for x in range(1000):
    lb.insert(END, x)
lb.pack(side=LEFT, fill=BOTH)
sb.config(command=lb.yview)

root.mainloop()
