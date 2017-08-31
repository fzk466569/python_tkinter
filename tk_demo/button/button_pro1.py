import tkinter as tk

root = tk.Tk()

GIRLS = ['西施', '懂事', '貂蝉']

v = []

for girl in GIRLS:
    v.append(tk.IntVar())
    b = tk.Checkbutton(root, text=girl, variable=v[-1])
    b.pack(anchor='w')

# l = tk.Label(root, textvariable=v)
# l.pack()
if __name__ == '__main__':
    tk.mainloop()
