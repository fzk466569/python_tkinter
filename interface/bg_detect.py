from tkinter import *
from tkinter.filedialog import askdirectory
import tkinter.messagebox
import threading
import inspect
import ctypes

from config.config import LANGUAGES
from api.file_api import target_match_file, format_filename
from api.send_msg import send_msg
from api.send_email import send_email


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    if not inspect.isclass(exctype):
        raise TypeError("Only types can be raised (not instances)")
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, 0)
        raise SystemError("PyThreadState_SetAsyncExc failed")


class Thread(threading.Thread):
    def _get_my_tid(self):
        """determines this (self's) thread id"""
        if not self.isAlive():
            raise threading.ThreadError("the thread is not active")
        # do we have it cached?
        if hasattr(self, "_thread_id"):
            return self._thread_id
        # no, look for it in the _active dict
        for tid, tobj in threading._active.items():
            if tobj is self:
                self._thread_id = tid
                return tid
        raise AssertionError("could not determine the thread's id")

    def raise_exc(self, exctype):
        """raises the given exception type in the context of this thread"""
        _async_raise(self._get_my_tid(), exctype)

    def terminate(self):
        """raises SystemExit in the context of the given thread, which should
        cause the thread to exit silently (unless caught)"""
        self.raise_exc(SystemExit)


# class Detect(object):
#     def __init__(self, v):
#         self.v = v
#         print('self.v: ', self.v)
#         self.root = Tk()
#
#         def selectPath():
#             path_value = askdirectory()
#             print(path_value)
#             dir_path.set(path_value)
#
#         dir_path = StringVar()
#
#         self.frame = LabelFrame(self.root, text='后台监听设置')
#         self.frame.pack(expand='yes', fill=BOTH, side=TOP)
#
#         Label(self.frame, text='监听目录:').grid(row=0, column=0, padx=5, pady=10)
#         Button(self.frame, text="路径选择", command=selectPath).grid(row=0, column=4, pady=10, sticky=E)
#         Label(self.frame, text='监听频率:').grid(row=1, column=0, padx=5, pady=10)
#
#         self.dirs = Entry(self.frame, textvariable=dir_path)
#         self.seconds = Entry(self.frame)
#
#         self.dirs.grid(row=0, column=1, columnspan=3, padx=5, pady=5)
#         self.seconds.grid(row=1, column=1, columnspan=3, padx=5, pady=5)
#
#         Button(self.frame, width=10, text='开始监听', command=self.start_detect).grid(row=2, column=1, pady=10, sticky=E)
#         Button(self.frame, width=10, text='停止监听', command=self.stop_detect).grid(row=2, column=2, pady=10, sticky=E)
#         self.frame.mainloop()
#
#     def detect(self, tel='18435155938', send_message=False, send_mail=True):
#         if self.dirs.get() and self.seconds.get():
#             path = self.dirs.get()
#             seconds = int(self.seconds.get())
#             # print(self.dirs.get(), self.seconds.get())
#             for x in detect(path, seconds):
#                 x = format_filename(x)
#                 # print('detect: ', x)
#                 target_script = []
#                 script = dict(script=dict(zip(LANGUAGES, [x for x in self.v])))
#                 for key, value in script.get('script').items():
#                     if value != 0:
#                         target_script.append(key)
#                 result_info = target_match_file(x, scripts=target_script)
#                 if result_info[0] == '危险':
#                     tkinter.messagebox.showinfo('Unsafe', '此文件危险：' + x)
#                     if send_message:
#                         send_data = dict(username='樊志魁', ip='127-0-0-1', filename=x)
#                         send_msg(send_data, tel)
#                     if send_mail:
#                         send_data = dict(username='樊志魁', ip='127-0-0-1', filename=x, target=result_info[1])
#                         send_email(send_data, )
#
#     def start_detect(self):
#         if self.dirs and self.seconds:
#             self.t = Thread(target=self.detect)
#             # self.t = threading.Thread(target=self.detect)
#             self.t.start()
#             print(self.t.isAlive())
#         else:
#             tkinter.messagebox._show('Error', '目录或者频率未设置')
#
#     def stop_detect(self):
#         try:
#             if self.t.isAlive():
#                 self.t.terminate()
#                 self.t.join()
#                 print(self.t.isAlive())
#         except:
#             tkinter.messagebox._show('Error', '没有开始监听哦')


# if __name__ == '__main__':
    # Detect([0, 0, 0, 1])
