import tkinter as tk
from tkinter import *

top = Tk()
top.geometry("400x400")
top.title("Stack")

class Stack:
    def __init__(self):
        self.element = []

    def push(self):
        self.element.append((text_Box.get(1.0, "end-1c")))
        text_Box.delete(1.0, "end")

    def pop(self):
        if len(self.element) > 0:
            self.element.pop()
        else:
            label.config(text="Stack is empty")

    def displayStack(self):
        if len(self.element) == 0:
            label.config(text="Stack is empty")
        else:
            r = "Stack: "
            for i in self.element:
                 r = r + i + ", "
            r = r[:-2]
            label.config(text=r)

def show(x):
    try:
        if x == "push":
            s1.push()
        elif x == "pop":
            s1.pop()
        elif x == "display":
            s1.displayStack()
    except Exception as e:
        label.config(text="There was an error")

text_Box = Text(top, height=2, width=20)
text_Box.place(x=130, y=50)

PushButton = Button(top, text="Push", width=10, height=2, command=lambda: show("push"))
PushButton.place(x=60, y=120)

PopButton = Button(top, text="Pop", width=10, height=2, command=lambda: show("pop"))
PopButton.place(x=160, y=120)

DisplayButton = Button(top, text="Display", width=10, height=2, command=lambda: show("display"))
DisplayButton.place(x=260, y=120)

label = Label(top, text="")
label.place(x=80, y=200)

s1 = Stack()

top.mainloop()


