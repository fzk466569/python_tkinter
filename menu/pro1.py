from tkinter import *

root = Tk()


def hello():
    print('hello')


def open_file():
    print('open_file')


def save_file():
    print('save_file')

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=False)
filemenu.add_command(label='打开', command=open_file)
filemenu.add_command(label='保存', command=save_file)
filemenu.add_separator()
filemenu.add_command(label='退出', command=root.quit)
menubar.add_cascade(label='文件', menu=filemenu)

editmenu = Menu(menubar, tearoff=False)
editmenu.add_command(label='剪切', command=hello)
editmenu.add_command(label='拷贝', command=hello)
editmenu.add_command(label='粘贴', command=hello)
menubar.add_cascade(label='编辑', menu=editmenu)

root.config(menu=filemenu)

root.mainloop()
