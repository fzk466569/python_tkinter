from tkinter import *

# 为了在某个足尖上安装垂直滚动条，需要做两件事
#   1.设置改组件的yscrollbarcommand选项为Scrollbar组件的set()方法
#   2.设置Scrollbar组件的command选项为盖组件的yview()方法

root = Tk()

Label(root, text='账号：').grid(row=0, column=0)
Label(root, text='密码：').grid(row=1, column=0)

v1 = StringVar()
v2 = StringVar()


def test(content):
    # 是数字就返回True，否则返回False
    return content.isdigit()


testCMD = root.register(test)

# validate=key时，将限制输入内容是否合法
e1 = Entry(root, textvariable=v1, validate='key', validatecommand=(testCMD, '%P'))
e2 = Entry(root, textvariable=v2, show='*')

e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)


def shaw():
    print('账号：《%s》' % e1.get())
    print('密码：《%s》' % e2.get())

Button(root, text='获取信息', width=10, command=shaw).grid(row=3, column=0, sticky=W, padx=10, pady=5)
Button(root, text='退出', width=10, command=root.quit).grid(row=3, column=1, sticky=E, padx=10, pady=5)

root.mainloop()
