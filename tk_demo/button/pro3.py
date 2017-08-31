from tkinter import *

root = Tk()

LANGS = [('python', 1), ('perl', 2), ('java', 3), ('ruby', 4)]

v = IntVar()
v.set(1)

for lang, num in LANGS:
    b = Radiobutton(root, text=lang, variable=v, value=num, indicatoron=False)
    b.pack(anchor='w', fill='x')

root.mainloop()
