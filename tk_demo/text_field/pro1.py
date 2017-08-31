from tkinter import *

root = Tk()

text = Text(root, width=50, height=30)
text.pack()

text.insert(INSERT, 'I Love U\n')
text.insert(END, 'RJP')

root.mainloop()
