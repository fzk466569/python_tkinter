#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/10 09:16
# Label
import tkinter as tk


def callback():
    var.set("吹吧你，我才不信呢~")


root = tk.Tk()

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)

# 创建一个文本Label对象
var = tk.StringVar()
var.set("您所下载的影片含有未成年人限制内容，\n请满18岁后再点击观看！")
textLabel = tk.Label(frame1,
                     textvariable=var,
                     justify=tk.LEFT)
textLabel.pack(side=tk.LEFT)

# 创建一个图像Label对象
# 用PhotoImage实例化一个图片对象（支持gif格式的图片）
photo = tk.PhotoImage(file="18.gif")
imgLabel = tk.Label(frame1, image=photo)
imgLabel.pack(side=tk.RIGHT)

# 加一个按钮
theButton = tk.Button(frame2, text="已满18周岁", command=callback)
theButton.pack()

frame1.pack(padx=10, pady=10)
frame2.pack(padx=10, pady=10)

tk.mainloop()
