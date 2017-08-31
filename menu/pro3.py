from tkinter import *

root = Tk()


def hello():
    print('hello')
menubar = Menu(root)

def donothing():
    pass

openVar = IntVar()
saveVar = IntVar()
quitVar = IntVar()

filemenu = Menu(root, tearoff=False)
filemenu.add_checkbutton(label='打开', command=hello, variable=openVar)
filemenu.add_checkbutton(label='保存', command=hello, variable=saveVar)
filemenu.add_separator()
filemenu.add_checkbutton(label='退出', command=root.quit, variable=quitVar)
menubar.add_cascade(label='文件', menu=filemenu)

editVar = IntVar()
editmenu = Menu(root, tearoff=False)
editmenu.add_radiobutton(label='剪切', command=hello, variable=editVar, value=1)
editmenu.add_radiobutton(label='拷贝', command=hello, variable=editVar, value=2)
editmenu.add_radiobutton(label='粘贴', command=hello, variable=editVar, value=3)
menubar.add_cascade(label='编辑', menu=editmenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)
menubar.add_cascade(label="Edit", menu=editmenu)
root.config(menu=menubar)

root.mainloop()
