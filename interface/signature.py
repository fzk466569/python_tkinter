from tkinter import *
import tkinter.messagebox
from tkinter.ttk import Treeview

from config.config import OPTION
from api.db import insert_data
from repository.common import DbCommon


class Signature(object):
    def __init__(self):
        self.singature_root = Tk()
        self.singature_root.title('基于webshell的校园网络安全系统--樊志魁')
        self.singature_root.iconbitmap('../images/title.ico')
        self.frame = LabelFrame(self.singature_root, text='增加特征码')

        tar_value = StringVar()

        Label(self.frame, text='类型：').grid(row=0, column=0, sticky=W, padx=5, pady=10)
        Label(self.frame, text='特征码：').grid(row=1, column=0, sticky=W, padx=5, pady=10)

        options_list = OPTION.keys()

        self.variable = StringVar()
        # 设置默认值
        self.variable.set('asp')
        om = OptionMenu(self.frame, self.variable, *options_list)
        om.grid(row=0, column=1, columnspan=2, padx=5, pady=10)

        self.value = Entry(self.frame, textvariable=tar_value, width=20)
        self.value.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

        Button(self.frame, text='提交', width=10, command=self.commit).grid(row=3, column=0, columnspan=3, sticky=W, pady=10, padx=10)
        Button(self.frame, text='取消', width=10, command=self.singature_root.quit).grid(row=3, column=2, columnspan=3, sticky=W, pady=10, padx=10)

        self.frame.grid(row=0, rowspan=8, column=0, columnspan=12)
        self.singature_root.mainloop()

    def commit(self):
        if self.variable.get() and self.value.get():
            table, value = self.variable.get(), self.value.get()
            if insert_data(table=table, data=dict(value=value)):
                tkinter.messagebox.showerror('success', '插入成功')
                self.value.delete(0, END)
            else:
                tkinter.messagebox.showerror('Error', '插入失败')
        else:
            tkinter.messagebox.showerror('Error', '忘记填值了？')


class ShowSignature(object):
    def __init__(self):
        self.singature_root = Tk()
        self.root_init(self.singature_root)

        top = LabelFrame(self.singature_root, text='查询分类', padx=5, pady=5, height=100, width=600)
        # top.pack(expand='yes', fill=X, side=TOP)
        top.grid(row=0, rowspan=8, column=0, columnspan=12)

        bottom = LabelFrame(self.singature_root, text='查询结果', padx=5, pady=5, height=300, width=795)
        # bottom.pack(expand='yes', fill=X, side=TOP)
        bottom.grid(row=10, rowspan=8, column=0, columnspan=12)

        self.top_init(top)
        self.bottom_init(bottom)
        self.singature_root.mainloop()

    def root_init(self, master):
        master.title('基于webshell的校园网络安全系统--樊志魁')
        master.iconbitmap('../images/title.ico')
        width, height = 520, 380
        screenwidth = master.winfo_screenwidth()
        screenheight = master.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        master.geometry(size)
        master.resizable(False, False)

    # 上面的frame
    def top_init(self, top):
        self.option = IntVar()
        self.option.set(0)
        value_list = ['asp', 'php', 'aspx', 'jsp', '数据库操作', '注册表', 'shell', '网络相关', '文件相关', 'web组件']
        pre_value = value_list[0:5]
        aft_value = value_list[-5:]
        print(pre_value, aft_value)
        for (option, value) in zip(pre_value, range(len(pre_value))):
            Radiobutton(top, text=option, variable=self.option, value=value).grid(row=0, column=value, padx=5)
        for (option, value) in zip(aft_value, range(len(aft_value))):
            Radiobutton(top, text=option, variable=self.option, value=value + 5).grid(row=1, column=value, padx=5)
        Button(top, text='提交', width=15, command=self.commit).grid(row=3, column=2, padx=5, sticky=W)
        Button(top, text='退出', width=15, command=self.singature_root.quit).grid(row=3, column=3, padx=5, sticky=E)
                # Radiobutton(top, text='Two', variable=v, value=2).pack(anchor='w')
            # Radiobutton(top, text='Three', variable=v, value=3).pack(anchor='w')

    def commit(self):
        x = self.tree.get_children()
        for item in x:
            self.tree.delete(item)
        dbc = DbCommon()
        # print(v.get())
        # print(value_list[v.get()])
        table = OPTION.get(list(OPTION.keys())[self.option.get()])
        for x in dbc.get_all_data(table):
            self.tree.insert('', END, value=x)

    # 下面的frame
    def bottom_init(self, bottom):
        scrollBar = Scrollbar(bottom)

        scrollBar.pack(side=RIGHT, fill=Y)

        # Treeview组件，6列，显示表头，带垂直滚动条
        self.tree = Treeview(bottom,
                             columns=('c1', 'c2', 'c3'),
                             show="headings",
                             height=10,
                             yscrollcommand=scrollBar.set)
        self.tree.column('c1', width=70, anchor='center')
        self.tree.column('c2', width=200, anchor='center')
        self.tree.column('c3', width=200, anchor='center')

        # 设置每列表头标题文本
        self.tree.heading('c1', text='ID')
        self.tree.heading('c2', text='特征码')
        self.tree.heading('c3', text='添加日期')

        self.tree.pack(side=LEFT, fill=Y)
        scrollBar.config(command=self.tree.yview)

        def treeviewClick(event):
            print('11111111111')

        self.tree.bind('<Return>', treeviewClick)
        # 赋值
        # for i in range(1, 20):
        #     tree.insert('', END, values=[i, 2, '安全', 4])

if __name__ == '__main__':
    Signature()
    # ShowSignature()
