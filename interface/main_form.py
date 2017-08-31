from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.ttk import Treeview
import tkinter.messagebox

from interface.settings import Settings
from api.file_api import target_match_path
from interface.bg_detect import Thread
from interface.signature import Signature, ShowSignature
from config.config import LANGUAGES


class MainForm(object):
    def __init__(self):
        self.root = Tk()
        self.root_init(self.root)
        menubar = self.create_menu(self.root)

        top = LabelFrame(self.root, text='配置信息', padx=8, pady=5, height=300, width=800)
        # top.pack(expand='yes', fill=X, side=TOP)
        top.grid(row=0, rowspan=8, column=0, columnspan=12)

        bottom = LabelFrame(self.root, text='扫描结果', padx=5, pady=5, height=300, width=795)
        # bottom.pack(expand='yes', fill=X, side=TOP)
        bottom.grid(row=10, rowspan=8, column=0, columnspan=12)

        self.top_init(top)
        self.bottom_init(bottom)
        self.root.config(menu=menubar)
        self.root.mainloop()

    def create_menu(self, root):
        menubar = Menu(root)

        filemenu = Menu(menubar, tearoff=False)
        filemenu.add_command(label='个人信息设置', command=self.set_settings)
        filemenu.add_command(label='导出扫描结果', command=self.output)
        filemenu.add_separator()
        filemenu.add_command(label='退出', command=quit)
        menubar.add_cascade(label='设置', menu=filemenu)

        signaturemenu = Menu(menubar, tearoff=False)
        # signaturemenu.add_separator()
        signaturemenu.add_command(label='添加特征码信息', command=self.add_signature)
        signaturemenu.add_command(label='查看现有特征码', command=self.show_signature)
        menubar.add_cascade(label='特征码', menu=signaturemenu)

        return menubar

    def add_signature(self):
        Signature()
        # s.root.quit()

    def show_signature(self):
        ShowSignature()
        # ss = ShowSignature()
        # self.root.wait_visibility(ss.singature_root)

    def root_init(self, master):
        master.title('基于webshell的校园网络安全系统--樊志魁')
        master.iconbitmap('../images/title.ico')
        width, height = 810, 620
        screenwidth = master.winfo_screenwidth()
        screenheight = master.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        master.geometry(size)
        master.resizable(False, False)

    # 上面的frame
    def top_init(self, top):
        # 路径选择
        def selectPath(path, path_value, ori_value=''):
            # path_ = askdirectory()
            path_value += ';' + ori_value
            print(path_value.replace('/', '\\'))
            path.set(path_value.replace('/', '\\'))

        # 开始扫描
        def start_scan():
            import time
            start = time.time()
            # map(self.tree.delete, self.tree.get_children())
            x = self.tree.get_children()
            for item in x:
                self.tree.delete(item)
            if self.v and targetdir.get():
                script = dict(script=dict(zip(LANGUAGES, [x.get() for x in self.v])))
                target_dir = dict(target_dir=targetdir.get().replace(';', '').replace('\\', '/'))
                trust_dirs = dict(trust_dirs=trustdirs.get().split(';')[:-1:])
                trust_type = dict(trust_type=trust_file_type.get().split(';'))
                target_script = []
                for key, value in script.get('script').items():
                    if value != 0:
                        target_script.append(key)

                for x in target_match_path(target_dir.get('target_dir'),
                                           [x.replace('\\', '/') for x in trust_dirs.get('trust_dirs')],
                                           trust_type.get('trust_type'), target_script):

                    self.tree.insert('', END, values=x)
                end = time.time()
                self.tree.insert('', END, value=[])
                self.tree.insert('', END, value=['', '', '本次扫描用时', '', end - start])
            else:
                tkinter.messagebox._show('Error', '是不是什么忘记填了？')

        # 停止扫描
        def stop_scan():
            pass

        def restart_scan():
            stop_scan()
            start_scan()

        def bg_detect(send_message=False, send_mail=True):
            from repository.common import DbCommon
            from api.send_msg import send_msg
            from api.send_email import send_email
            from api.file_api import format_filename, detect, target_match_file

            dbc = DbCommon()
            tel = dbc.get_all_data_column('settings', 'phone')[0]
            email = dbc.get_all_data_column('settings', 'email')
            host = dbc.get_all_data_column('settings', 'host')[0]
            user = dbc.get_all_data_column('settings', 'user')[0]
            # 18435155938 fzk46669@163.com
            print([x.get() for x in self.v])
            if self.v and targetdir.get():
                script = dict(script=dict(zip(LANGUAGES, [x.get() for x in self.v])))
                target_dir = dict(target_dir=targetdir.get().replace(';', '').replace('\\', '/'))
                trust_dirs = dict(trust_dirs=[x.replace('\\', '/') for x in trustdirs.get().split(';')[:-1:]])
                trust_type = dict(trust_type=trust_file_type.get().split(';'))
                seconds = int(self.seconds.get())
                target_script = []
                for key, value in script.get('script').items():
                    if value != 0:
                        target_script.append(key)

                print(target_dir, trust_dirs, trust_type, target_script, seconds)
                for x in detect(target_dir.get('target_dir'), seconds):
                    x = format_filename(x)
                    # print('detect: ', x)
                    target_script = []
                    script = dict(script=dict(zip(LANGUAGES, [x for x in self.v])))
                    for key, value in script.get('script').items():
                        if value != 0:
                            target_script.append(key)
                    result_info = target_match_file(x, scripts=target_script)
                    print('result_info:', result_info)
                    if result_info[0] == '危险':

                        if send_message:
                            # print('main_form_message:00000000000000000000000000')
                            host = host.replace('.', '-')
                            send_data = dict(username=user, ip=host, filename=x)
                            send_msg(send_data, tel)

                        if send_mail:
                            # print('main_form_email:1111111111111111111111111')
                            send_data = dict(username=user, ip=host, filename=x, target=result_info[1])
                            print('main_form_email:', email)
                            send_email(send_data, address=email)
                        tkinter.messagebox.showinfo('Unsafe', '此文件危险：' + x)

            # Detect([x.get() for x in self.v])

        def start_detect():
            if targetdir.get() and self.seconds.get() and len(self.v) > 0:
                self.t = Thread(target=bg_detect)
                # self.t = threading.Thread(target=self.detect)
                self.t.start()
                print(self.t.isAlive())
            else:
                tkinter.messagebox._show('Error', '目录或者频率未设置')

        def stop_detect():
            try:
                if self.t.isAlive():
                    self.t.terminate()
                    self.t.join()
                    print(self.t.isAlive())
            except:
                tkinter.messagebox._show('Error', '没有开始监听哦')

        dir_path = StringVar()
        trust_path = StringVar()
        seconds = IntVar()
        seconds.set(1)

        Label(top, text="目标路径:").grid(row=0, column=0, columnspan=1, padx=5, pady=10, sticky=W)
        targetdir = Entry(top, textvariable=dir_path, width=90)
        targetdir.grid(row=0, column=1, columnspan=8, padx=5, pady=10)
        targetdir.insert(INSERT, 'I:\\bishe\\web;')
        Button(top, text="路径选择", command=lambda: selectPath(path=dir_path, path_value=askdirectory())).grid(row=0,
                                                                                                            column=10,
                                                                                                            columnspan=1,
                                                                                                            padx=5,
                                                                                                            pady=10)

        Label(top, text="信任区:").grid(row=2, column=0, columnspan=1, padx=5, pady=10, sticky=W)
        trustdirs = Entry(top, textvariable=trust_path, width=90)
        trustdirs.grid(row=2, column=1, columnspan=8, padx=5, pady=10)
        trustdirs.insert(INSERT, '')
        Button(top, text="路径选择",
               command=lambda: selectPath(path=trust_path, path_value=askdirectory(), ori_value=trustdirs.get())).grid(
            row=2, column=10, columnspan=1, padx=5, pady=10)

        Label(top, text='扫描类型:').grid(row=3, column=0, padx=5, pady=10, sticky=W)
        self.v = []
        row, column = 3, 1
        for language in LANGUAGES:
            self.v.append(IntVar())
            b = Checkbutton(top, text=language, variable=self.v[-1])
            b.grid(row=row, column=column, sticky=W, padx=10)
            column += 1

        Label(top, text='信任的文件类型:').grid(row=4, padx=5, columnspan=2, pady=10, sticky=W)
        trust_file_type = Entry(top, width=70)
        trust_file_type.grid(row=4, column=2, padx=5, pady=10, columnspan=6)
        trust_file_type.insert(0, 'mp3;mp4;avi')

        Button(top, text='开始扫描', command=start_scan).grid(row=5, column=1, padx=5, pady=15, sticky=W)
        Button(top, text='停止扫描', command=stop_scan).grid(row=5, column=2, padx=20, pady=15, sticky=W)
        Button(top, text='重新扫描', command=restart_scan).grid(row=5, column=3, padx=20, pady=15, sticky=W)
        Button(top, text='开始监听', command=start_detect).grid(row=5, column=7, padx=10, pady=15, sticky=W)
        Button(top, text='停止监听', command=stop_detect).grid(row=5, column=8, padx=10, pady=15, sticky=W)
        Label(top, text='监听频率：').grid(row=5, column=5)
        self.seconds = Entry(top, textvariable=seconds, width=5)
        self.seconds.grid(row=5, column=6)

    # 下面的frame
    def bottom_init(self, bottom):
        scrollBar = Scrollbar(bottom)

        scrollBar.pack(side=RIGHT, fill=Y)

        # Treeview组件，6列，显示表头，带垂直滚动条
        self.tree = Treeview(bottom,
                             columns=('c1', 'c2', 'c3',
                                      'c4', 'c5'),
                             show="headings",
                             height=13,
                             yscrollcommand=scrollBar.set)
        self.tree.column('c1', width=50, anchor='center')
        self.tree.column('c2', width=395, anchor=W)
        self.tree.column('c3', width=130, anchor='center')
        self.tree.column('c4', width=50, anchor='center')
        self.tree.column('c5', width=150, anchor='center')

        # 设置每列表头标题文本
        self.tree.heading('c1', text='ID')
        self.tree.heading('c2', text='文件路径')
        self.tree.heading('c3', text='最后修改日期')
        self.tree.heading('c4', text='状态')
        self.tree.heading('c5', text='备注')
        self.tree.pack(side=LEFT, fill=Y)
        scrollBar.config(command=self.tree.yview)

        def treeviewClick(event):
            print('11111111111')

        self.tree.bind('<Return>', treeviewClick)
        # 赋值
        # for i in range(1, 20):
        #     tree.insert('', END, values=[i, 2, '安全', 4])

    # 跳到settings页面
    def set_settings(self):
        Settings()

    def output(self):
        x = self.tree.get_children()
        print(x)
        for item in x:
            print(self.tree.get_children(item))


if __name__ == '__main__':
    MainForm()
