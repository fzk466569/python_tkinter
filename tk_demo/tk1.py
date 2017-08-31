#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/9 17:35

import tkinter as tk


class APP(object):
    def __init__(self, master):
        frame = tk.Frame(master)
        # side 设置向哪对齐，pad边界值，x横向，y纵向
        frame.pack(side=tk.LEFT, padx=10, pady=10)
        self.hi_there = tk.Button(frame, text='how are u', fg='blue', command=self.say_hi)
        self.hi_there.pack()

    def say_hi(self):
        print('HOW R U')


if __name__ == '__main__':
    root = tk.Tk()
    app = APP(root)
    root.mainloop()
