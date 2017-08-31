from tkinter import *

root = Tk()

photo = PhotoImage(file="bg.gif")
theLabel = Label(root,
                 text="tkinter",
                 justify=LEFT,      # 左对齐
                 image=photo,       # 背景图
                 compound=CENTER,   # 字体在图片正上方
                 font=("simsun.ttc", 20),
                 fg="white"         # 前景色，也就是字体色
                 )
theLabel.pack()

mainloop()
