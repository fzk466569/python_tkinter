from tkinter import *

m1 = PanedWindow(showhandle=True, sashrelief=SUNKEN)
m2 = PanedWindow(orient=VERTICAL, showhandle=True, sashrelief=SUNKEN)
m1.pack(fill=BOTH, expand=1)

left = Label(m1, text='left')
m1.add(left)

m1.add(m2)

top = Label(m2, text="top")
m2.add(top)

buttom = Label(m2, text='buttom')
m2.add(buttom)

mainloop()
