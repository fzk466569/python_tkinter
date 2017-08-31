from tkinter import *
import tkinter.messagebox
from repository.common import DbCommon


class Settings(object):
    def __init__(self):
        self.root = Tk()
        self.root.iconbitmap('../images/title.ico')
        self.root.title('基于webshell的校园网络安全系统--樊志魁')
        self.frame = LabelFrame(self.root, text='用来接收结果信息的手机和邮箱')
        self.frame.pack(expand='yes', fill=BOTH, side=TOP)

        Label(self.frame, text='邮箱:').grid(row=0, column=0, padx=5, pady=10)
        Label(self.frame, text='手机:').grid(row=1, column=0, padx=5, pady=10)
        Label(self.frame, text='服务器:').grid(row=2, column=0, padx=5, pady=10)

        self.email = Entry(self.frame)
        self.phone = Entry(self.frame)
        self.host = Entry(self.frame)

        self.email.grid(row=0, column=1, columnspan=3, padx=5, pady=5)
        self.phone.grid(row=1, column=1, columnspan=3, padx=5, pady=5)
        self.host.grid(row=2, column=1, columnspan=3, padx=5, pady=5)

        Button(self.frame, width=10, text='提   交', command=self.commit).grid(row=3, column=1, pady=10, sticky=E)
        self.frame.mainloop()

    def commit(self):
        import re
        email = self.email.get()
        phone = self.phone.get()
        host = self.host.get()

        re_phone = re.compile('^1[3,4,5,7,8]\d{9}$')
        re_email = re.compile('^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$')
        if re_phone.match(phone) and re_email.match(email) and host:
            print(phone, email)
            data = dict(phone=phone, email=email, host=host, user='fzk')
            dbc = DbCommon()
            dbc.update_data('settings', data=data, origin='user')
            self.root.destroy()
        else:
            tkinter.messagebox._show('Error', '邮箱或手机号非法')

if __name__ == '__main__':
    Settings()
