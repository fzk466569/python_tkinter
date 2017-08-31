from tkinter import *

root = Tk()

w = PanedWindow(root, orient=VERTICAL)
w.pack(fill=BOTH, expand=1)

top = Label(w, text='top')
w.add(top)

buttom = Label(w, text='buttom')
w.add(buttom)

root.mainloop()
