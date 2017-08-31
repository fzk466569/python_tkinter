from tkinter import *

root = Tk()
text = Text(width=50, height=30)
text.pack()

text.insert(INSERT, 'I LOVE U')
text.insert(END, 'RJP')

photo = PhotoImage(file='../18.gif')


def show():
    text.image_create(INSERT, image=photo)
    print('点我干嘛')

b1 = Button(text, text='点我', command=show)
text.window_create(END, window=b1)

root.mainloop()
