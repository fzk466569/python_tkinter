from tkinter import *

root = Tk()


def hello():
    print('hello')

# RAISED 按钮的样式
menubut = Menubutton(root, text='点我', relief=RAISED)
menubut.pack()
menubar = Menu(menubut, tearoff=False)

filemenu = Menu(menubar, tearoff=False)
filemenu.add_command(label='打开', command=hello)
filemenu.add_command(label='保存', command=hello)
filemenu.add_separator()
filemenu.add_command(label='退出', command=root.quit)
menubar.add_cascade(label='文件', menu=filemenu)

menubut.config(menu=filemenu)

root.mainloop()
