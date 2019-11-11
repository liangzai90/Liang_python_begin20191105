print("----------- tkinter 模块，编写一个文本编辑器--------")
from tkinter import *
from tkinter.scrolledtext import ScrolledText

def load():
    with open(filename.get()) as file:
        contents.delete('1.0', END)
        contents.insert(INSERT, file.read())

def save():
    with open(filename.get(), 'w') as file:
        file.write(contents.get('1.0', END))

top = Tk()
top.title("Simple Editor")

contents = ScrolledText()
contents.pack(side=BOTTOM, expand=True, fill=BOTH)

filename = Entry()
filename.pack(side=LEFT, expand=True, fill=X)

Button(text="Open", command=load).pack(side=LEFT)
Button(text="Save", command=save).pack(side=LEFT)

mainloop()

"""
后续可以继续扩展功能。例如，更加抽象、让这个程序使用模块urllib下载文件等
"""
