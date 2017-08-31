from tkinter import *

root = Tk()

w = Canvas(root, width=500, height=300)
w.pack()

w.create_line(0, 150, 300, 150, fill='yellow')
w.create_line(100, 0, 100, 100, fill='red', dash=(4, 4))
# w.create_line()

root.mainloop()
