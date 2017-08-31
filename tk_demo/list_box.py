from tkinter import *

root = Tk()

theLB = Listbox(root, selectmod=SINGLE)     # SINGLE EXTENDED
theLB.pack()

theLB.insert(0, 'pig')
theLB.insert(1, 'pig')
theLB.insert(2, 'pig')
theLB.insert(END, 'pig')

for item in ['鸡蛋', '丫蛋', '狗蛋', '鸟蛋']:
    theLB.insert(END, item)

theBut = Button(root, text='删除它', command=lambda x=theLB: x.delete(ACTIVE))
theBut.pack()

root.mainloop()
