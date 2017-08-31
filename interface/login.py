from tkinter import *
import tkinter.messagebox

from repository.user import login_check
from interface.main_form import MainForm


class Login(object):
    def __init__(self):
        self.login = Tk()
        self.login.title('基于webshell的校园网络安全系统')
        self.login.iconbitmap('../images/title.ico')

        input = LabelFrame(self.login, text='输入你的个人账号', padx=5, pady=5)
        input.pack(padx=10, pady=10)

        Label(input, text='账号:').grid(row=0, column=0, sticky=W, padx=5, pady=10)
        Label(input, text='密码:').grid(row=1, column=0, sticky=W, padx=5, pady=10)

        self.username = Entry(input)
        self.username.grid(row=0, column=1, padx=5, pady=10)
        self.password = Entry(input, show='*')
        self.password.grid(row=1, column=1, padx=5, pady=10)

        commit = Button(input, text='提交', width=10,
               command=self.confirm)
        commit.grid(row=2, columnspan=3, pady=5)

        mainloop()

    def confirm(self):
        name = self.username.get()
        passwd = self.password.get()
        if login_check(name, passwd):
            self.login.destroy()
            # self.login.withdraw()
            MainForm()
        else:
            tkinter.messagebox._show(title='ERROR！', message='账号或密码错误')


if __name__ == '__main__':
    Login()
